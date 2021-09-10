import os

# this file used to setup the logging infrastructure (dirs/files)

training_log_files = ["valuesfromSchemaValidationLog" , "GeneralLog" , "nameValidationLog" ,
                      "columnValidationLog","missingValuesInColumn"  , "DataBaseConnectionLog" , "DBInsertLog" ,
                      "TrainingMainLog" , "DataTransformLog" , "ModelTrainingLog" , "DataTransform"]

#prediction_log_files = ['DataBaseConnectionLog' ,"valuesfromSchemaValidationLog","nameValidationLog" ,"ExportTOCSV" ,
 #                     "PredictionLog" , 'DBtableCreateLog' , "missingValuesInColumn","DataTransform","DBInsertLog"]

prediction_log_files = ["PredictionLog"]


class LogsDirFileGenerator:
    def __init__(self , training_log_files ,prediction_log_files):
        self.training_log_files = training_log_files
        self.prediction_log_files = prediction_log_files
        self.training_logs_dir = 'Training_Logs'
        self.prediction_logs_dir = 'Prediction_Logs'


    def create_log_dirs(self):
        '''
                :Task : Create the Training and prediction Logs dir
                :By : Shubham Chau
        '''
        try :
            os.makedirs(self.training_logs_dir , exist_ok=True)
            os.makedirs(self.prediction_logs_dir ,exist_ok=True)
        except Exception as e:
            return  e

    def create_Training_LogsFiles(self):
        '''
                task : create the LogFiles to store training Info.
                By : Shubham Chau
        '''
        for file_ in self.training_log_files:
            try:
                with open(os.path.join(self.training_logs_dir , file_ + '.txt') ,  mode='w') as f :
                    f.close()
            except Exception as e :
                return e

    def create_Prediction_LogsFiles(self):
        '''
                :Task : Create the PresictionLogs files
                By : Shubham Chau
        '''
        for file_ in self.prediction_log_files:
            try:
                with open(os.path.join( self.prediction_logs_dir , file_ + '.txt') ,  mode='w') as f :
                    f.close()
            except Exception as e :
                return e






if __name__ == '__main__':
    a = LogsDirFileGenerator(training_log_files=training_log_files , prediction_log_files=prediction_log_files)
    a.create_log_dirs()
    a.create_Training_LogsFiles()
    a.create_Prediction_LogsFiles()





