from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import GridSearchCV
from xgboost import XGBClassifier
from sklearn.metrics  import roc_auc_score,accuracy_score
from application_logging.logging import logger_app
import numpy as np
import warnings
warnings.filterwarnings("ignore")

class Model_Finder:
    """
                This class shall  be used to find the model with best accuracy and AUC score.
                written by : Vikas  
    """
    def __init__(self):
        self.logFilepath = "Training_Logs/ModelTrainingLog.txt"
        self.logger_object = logger_app()
        self.ran = RandomForestClassifier()
        self.xgb = XGBClassifier(random_state = 30 , learning_rate = 0.01,eval_metric='mlogloss')

    def get_best_params_for_random_forest(self,train_x,train_y):
        """
            Method Name: get_best_params_for_random_forest
            Description: get the parameters for the Random Forest Classifier Algorithm which give the best accuracy.Use Hyper Parameter Tuning.
            Output: The model with the best parameters
            On Failure: Raise Exception
            version : 0.1
        """
        self.logfile = open(self.logFilepath , mode='a')
        self.logger_object.log(self.logfile, 'Entered the get_best_params_for_random_forest method of the Model_Finder class')
        try:
            # Number of trees in random forest
            n_estimators = [int(x) for x in np.linspace(start=200, stop=2000, num=10)]
            # Number of features to consider at every split
            max_features = ['auto', 'sqrt', 'log2']
            # Maximum number of levels in tree
            max_depth = [int(x) for x in np.linspace(10, 1000, 10)]
            # Minimum number of samples required to split a node
            min_samples_split = [2, 5, 10, 14]
            # Minimum number of samples required at each leaf node
            min_samples_leaf = [1, 2, 4, 6, 8]
            # Create the random grid
            self.random_grid = {'n_estimators': n_estimators,
                           'max_features': max_features,
                           'max_depth': max_depth,
                           'min_samples_split': min_samples_split,
                           'min_samples_leaf': min_samples_leaf,
                           'criterion': ['entropy', 'gini']
                           }

            #Creating an object of the Grid Search class
            self.grid = RandomizedSearchCV(estimator=self.ran, param_distributions=self.random_grid, n_iter=10, cv=2, verbose=2,
                                             random_state=100, n_jobs=20)
            #finding the best parameters
            self.grid.fit(train_x, train_y)

            # extracting the best parameters
            self.max_depth = self.grid.best_params_['max_depth']
            self.n_estimators = self.grid.best_params_['n_estimators']
            self.max_features = self.grid.best_params_['max_features']
            self.min_samples_leaf = self.grid.best_params_['min_samples_leaf']
            self.min_samples_split = self.grid.best_params_['min_samples_split']
            self.criterion = self.grid.best_params_['criterion']


            #creating a new model with the best parameters
            self.ran = RandomForestClassifier(criterion = self.criterion,max_depth=self.max_depth,n_estimators= self.n_estimators,max_features = self.max_features,min_samples_leaf = self.min_samples_leaf,min_samples_split =  self.min_samples_split)
            # training the mew model
            self.ran.fit(train_x, train_y)
            self.logger_object.log(self.logfile,'Random Forest Classifier best params: '+str(self.grid.best_params_)+'. Exited the get_best_params_for_random_forest method of the Model_Finder class')
            self.logfile.close()
            return self.ran
        except Exception as e:
            self.logger_object.log(self.logfile,'Exception occured in get_best_params_for_random_forest method of the Model_Finder class. Exception message:  ' + str(e))
            self.logger_object.log(self.logfile,'Random Forest Classifier Parameter tuning  failed. Exited the get_best_params_for_random_forest method of the Model_Finder class')
            self.logfile.close()
            raise Exception()

    def get_best_params_for_xgboost(self,train_x,train_y):

        """
            Method Name: get_best_params_for_xgboost
            Description: get the parameters for XGBoost Algorithm which give the best accuracy.Use Hyper Parameter Tuning.
            Output: The model with the best parameters
            On Failure: Raise Exception
            Written By: vikas 
        """
        self.logfile = open(self.logFilepath , mode='a')
        self.logger_object.log(self.logfile,'Entered the get_best_params_for_xgboost method of the Model_Finder class')
        try:
            # initializing with different combination of parameters
            self.param_grid_xgboost = {
                'learning_rate': [0.1, 0.01, 0.001, 0.05],
                'max_depth': [5, 10, 15, 20],
                'n_estimators': [10, 50, 100, 200]
            }
            # Creating an object of the Grid Search class
            self.grid= GridSearchCV(XGBClassifier(random_state = 30 , eval_metric='mlogloss'),self.param_grid_xgboost, verbose=3,cv=2,n_jobs=-1)
            # finding the best parameters
            self.grid.fit(train_x, train_y)

            # extracting the best parameters
            self.learning_rate = self.grid.best_params_['learning_rate']
            self.max_depth = self.grid.best_params_['max_depth']
            self.n_estimators = self.grid.best_params_['n_estimators']

            # creating a new model with the best parameters
            self.xgb = XGBClassifier(learning_rate=self.learning_rate, max_depth=self.max_depth,n_estimators= self.n_estimators, n_jobs=-1 )
            # training the mew model
            self.xgb.fit(train_x, train_y)
            self.logger_object.log(self.logfile,'XGBoost best params: ' + str(self.grid.best_params_) + '. Exited the get_best_params_for_xgboost method of the Model_Finder class')
            self.logfile.close()
            return self.xgb

        except Exception as e:
            self.logger_object.log(self.logfile,'Exception occured in get_best_params_for_xgboost method of the Model_Finder class. Exception message:  ' + str(e))
            self.logger_object.log(self.logfile,'XGBoost Parameter tuning  failed. Exited the get_best_params_for_xgboost method of the Model_Finder class')
            self.logfile.close()
            raise Exception()


    def get_best_model(self,train_x,train_y,test_x,test_y):

        """
            Method Name: get_best_model
            Description: Find out the Model which has the best AUC score.
            Output: The best model name and the model object
            On Failure: Raise Exception
        
        """
        self.logfile = open(self.logFilepath , mode='a')
        self.logger_object.log(self.logfile,'Entered the get_best_model method of the Model_Finder class')

        # create best model for XGBoost
        try:
            self.xgboost= self.get_best_params_for_xgboost(train_x,train_y)
            self.prediction_xgboost = self.xgboost.predict(test_x)
            # Predictions using the XGBoost Model

            if len(test_y.unique()) == 1:
            #if there is only one label in y, then roc_auc_score returns error. We will use accuracy in that case
                self.xgboost_score = accuracy_score(test_y, self.prediction_xgboost)
                self.logger_object.log(self.logfile, 'Accuracy for XGBoost Model :' + str(self.xgboost_score))
                
                # Log AUC
            else:
                self.xgboost_score = roc_auc_score(test_y, self.prediction_xgboost)
                # AUC for XGBoost
                self.logger_object.log(self.logfile, 'AUC for XGBoost:' + str(self.xgboost_score))
                # Log AUC

            # create best model for Random Forest
            self.ran=self.get_best_params_for_random_forest(train_x,train_y)
            self.prediction_random_forest=self.ran.predict(test_x)
            # prediction using the Random Forest Algorithm

            if len(test_y.unique()) == 1:
                #if there is only one label in y, then roc_auc_score returns error. We will use accuracy in that case
                self.random_forest_score = accuracy_score(test_y,self.prediction_random_forest)
                self.logger_object.log(self.logfile, 'Accuracy for Random Forest Model :' + str(self.random_forest_score))
            else:
                self.random_forest_score = roc_auc_score(test_y, self.prediction_random_forest) # AUC for Random Forest
                self.logger_object.log(self.logfile, 'AUC for Random forest Model :' + str(self.random_forest_score))

            #comparing the two models
            if(self.random_forest_score <  self.xgboost_score):
                return 'XGBoost',self.xgboost
            else:
                return 'Random Forest',self.ran

            self.logfile.close()

        except Exception as e:
            self.logger_object.log(self.logfile,'Exception occured in get_best_model method of the Model_Finder class. Exception message:  ' + str(e))
            self.logger_object.log(self.logfile,'Model Selection Failed. Exited the get_best_model method of the Model_Finder class')
            self.logfile.close()
            raise Exception()

