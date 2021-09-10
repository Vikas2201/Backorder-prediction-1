import pickle
import os
import shutil
from application_logging.logging import logger_app


class Model_Operation:
    """
        This class shall be used to save the model after training and load the saved model for prediction.
        writtn by :Vikas 
    """

    def __init__(self):
        self.LogfilePath = "Training_Logs/ModelTrainingLog.txt"
        self.logger_object = logger_app()
        self.model_directory='Model/'

    def save_model(self,model,filename):
        """
            Method Name: save_model
            Description: Save the model file to directory
            Outcome: File gets saved
            On Failure: Raise Exception
        """

        self.logfile  = open(self.LogfilePath , mode='a')
        self.logger_object.log(self.logfile, 'Entered the save_model method of the Model_Operation class')
        try:
            path = os.path.join(self.model_directory,filename)
            #create separate directory for each cluster
            if os.path.isdir(path):
                #remove previously existing models for each clusters
                shutil.rmtree(self.model_directory)
                os.makedirs(path)
            else:
                os.makedirs(path)
            with open(path +'/' + filename+'.sav','wb') as f:
                pickle.dump(model, f) # save the model to file
            self.logger_object.log(self.logfile,'Model File '+filename+' saved. Exited the save_model method of the Model_Finder class')
            self.logfile.close()
            return 'success'

        except Exception as e:
            self.logger_object.log(self.logfile,'Exception occured in save_model method of the Model_Finder class. Exception message:  ' + str(e))
            self.logger_object.log(self.logfile,'Model File '+filename+' could not be saved. Exited the save_model method of the Model_Finder class')
            self.logfile.close()
            raise Exception()

    def load_model(self,filename):
        """
            Method Name: load_model
            Description: load the model file to memory
            Output: The Model file loaded in memory
            On Failure: Raise Exception
        """
        self.logfile  = open(self.LogfilePath , mode='a')
        self.logger_object.log(self.logfile, 'Entered the load_model method of the Model_Operation class')
        try:
            with open(self.model_directory + filename + '/' + filename + '.sav','rb') as f:
                self.logger_object.log(self.logfile,'Model File ' + filename + ' loaded. Exited the load_model method of the Model_Finder class')
                self.logfile.close()
                return pickle.load(f)

        except Exception as e:
            self.logger_object.log(self.logfile,'Exception occured in load_model method of the Model_Finder class. Exception message:  ' + str(e))
            self.logger_object.log(self.logfile,'Model File ' + filename + ' could not be saved. Exited the load_model method of the Model_Finder class')
            self.logfile.close()
            raise Exception()

    def find_correct_model_file(self):
        """
            Method Name: find_correct_model_file
            Description: Select the correct model From Directory
            Output: The Model file
            On Failure: Raise Exception
        """
        self.logfile  = open(self.LogfilePath , mode='a')
        self.logger_object.log(self.logfile,'Entered the find_correct_model_file method of the Model_Operation class')
        try:
            # self.cluster_number= cluster_number
            self.folder_name = self.model_directory
            self.list_of_files = []
            self.list_of_files = os.listdir(self.folder_name)
            for self.file in self.list_of_files:
                try:
                    self.model_name = self.file
                except:
                    continue
            self.model_name = self.model_name.split('.')[0]
            self.logger_object.log(self.logfile,'Exited the find_correct_model_file method of the Model_Operation class.')
            self.logfile.close()
            return self.model_name
        except Exception as e:
            self.logger_object.log(self.logfile,'Exception occured in find_correct_model_file method of the Model_Operation class. Exception message:  ' + str(e))
            self.logger_object.log(self.logfile,'Exited the find_correct_model_file method of the Model_Operation class with Failure')
            self.logfile.close()
            raise Exception()
