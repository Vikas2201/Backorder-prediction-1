import pandas as pd
from application_logging.logging import logger_app
import warnings
warnings.filterwarnings("ignore")

class Data_Getter:
    """
    This class shall  be used for obtaining the data from the source for training.
    written by : Vikas 
    modifried by : Shubham 
    modification : changes in File code ( removed buffering..)
    """
    def __init__(self):
        self.training_file='Training_FileFromDB/InputFile.csv' #Input File Link
        self.predict_data = 'Prediction_Output_File/Predictions.csv' #Prediction file link
        self.logfilepath="Training_Logs/GeneralLog.txt"
        self.logger_object=logger_app()

    def get_data(self):
        """
        Method Name: get_data
        Description: This method reads the data from source.
        Output: A pandas DataFrame.
        On Failure: Raise Exception
        """
        self.logfile = open(self.logfilepath ,mode='a')
        self.logger_object.log(self.logfile,'Entered the get_data method of the Data_Getter class')
        try:
            self.data= pd.read_csv(self.training_file) # reading the data file
            self.logger_object.log(self.logfile,'Data Load Successful.Exited the get_data method of the Data_Getter class')
            self.logfile.close()
            return self.data

        except Exception as e:
            self.logger_object.log(self.logfile,'Exception occured in get_data method of the Data_Getter class. Exception message: '+str(e))
            self.logger_object.log(self.logfile,'Data Load Unsuccessful.Exited the get_data method of the Data_Getter class')
            self.logfile.close()
            raise Exception()

    def prediction_data(self):
        """
                Method Name: prediction_data
                Description: This method reads the data from source.
                Output: A pandas DataFrame.
                On Failure: Raise Exception
        """
        self.logfile = open(self.logfilepath ,mode='a')
        self.logger_object.log(self.logfile, 'Entered the Prediction_data method of the Data_Getter class')
        try:
            self.data = pd.read_csv(self.predict_data)  # reading the data file
            self.logger_object.log(self.logfile,'Data Load Successful.Exited the Prediction_data method of the Data_Getter class')
            self.logfile.close()
            return self.data

        except Exception as e:
            self.logger_object.log(self.logfile,'Exception occured in Prediction_data method of the Data_Getter class. Exception message: ' + str(e))
            self.logger_object.log(self.logfile,'Data Load Unsuccessful.Exited the Prediction_data method of the Data_Getter class')
            self.logfile.close()
            raise Exception()
