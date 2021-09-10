from scipy.stats.stats import mode
from data_ingestion import data_loader
from data_perprocessing import preprocessing
from Model_Finder import Model
from Save_Model import save_methods
from sklearn.model_selection import train_test_split
from application_logging.logging import logger_app
import warnings
warnings.filterwarnings("ignore")

"""
This is the for Training the Machine Learning Model.
"""

class training:

    def __init__(self):
        self.logger = logger_app()
    def trainingModel(self):
        self.file = open('Training_Logs/ModelTrainingLog.txt' , mode='a')
        self.logger.log(self.file , "Training Operation Started....")
        try:
            # Getting the data from the source
            data_getter=data_loader.Data_Getter()
            data=data_getter.get_data()
            #data preprocessing

            preprocessor=preprocessing.Preprocessor()

            # remove the unnamed column as it doesn't contribute to prediction.
            data = preprocessor.remove_columns(data,["sku","national_inv","lead_time","in_transit_qty","min_bank","potential_issue","pieces_past_due","local_bo_qty","deck_risk","oe_constraint","ppap_risk","stop_auto_buy","rev_stop"])
            ##Convert categorical values to numeric values
            data = preprocessor.encode_categorical_columns(data)

            # check if missing values are present in the dataset
            is_null_present,cols_with_missing_values = preprocessor.is_null_present(data)

            # if missing values are there, replace them appropriately.
            if (is_null_present):
                data = preprocessor.impute_missing_values(data,cols_with_missing_values) # missing value imputation


            # create separate features and labels
            X , Y = preprocessor.separate_label_feature(data,label_column_name='went_on_backorder')

            #scaling the X values
            X = preprocessor.scale_numerical_columns(X)

            #Imbalanced dataset to make it a balanced one
            X , Y = preprocessor.handle_imbalanced_dataset(X,Y)


            ## parsing all the clusters and looking for the best ML algorithm to fit on individual cluster
            x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=1 / 3, random_state=355)

            # object initialization
            model_finder = Model.Model_Finder() 

            # Getting the best model for each of the clusters
            best_model_name,best_model = model_finder.get_best_model(x_train,y_train,x_test,y_test)

            #saving the best model to the directory.
            model_op = save_methods.Model_Operation()
            save_model = model_op.save_model(best_model, best_model_name)   
            self.logger.log(self.file , "Training Operation Completed SuccessFully....")
            self.file.close()             


        except Exception as e :
            # logging the unsuccessful Training
            self.logger.log(self.file, 'class : training , filelocation : trainingfile.py : Unsuccessful End of Training' + str(e))
            self.file.close()
            raise e
