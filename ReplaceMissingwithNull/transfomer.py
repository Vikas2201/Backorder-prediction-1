from application_logging.logging import logger_app
import pandas as pd
import numpy as np
import os


class Transform :
    def __init__(self):
        self.logger = logger_app()
        self.dirpath = "Training_Raw_files_validated/Good_Raw"

    def convertMissingtonull(self):
        '''
            Method : convertMissingtonull
            Aim : This method will convert Missing value into the Null Value

            :return: None
        '''
        logger_file = open('Training_Logs/TrainingMainLog.txt' , mode='a')
        self.logger.log(logger_file , "Replacing Missing Value by NULL ")
        try :
            filenames = [x for x in os.listdir(self.dirpath)]
            for file in filenames:
                file_path = os.path.join(self.dirpath, file)
                df = pd.read_csv(file_path)
                df.fillna( np.nan , inplace=True)
                # export data to csv
                df.to_csv(self.dirpath + "/" + file, index=None, header=True)
                self.logger.log( logger_file, " %s: File Transformed successfully!!" % file)

            logger_file.close()

        except Exception as e:
            self.logger.log(logger_file, "Exception during Transforming missing by NULL ")
            self.logger.log(logger_file, f"Exception : {str(e)} ")
            logger_file.close()




