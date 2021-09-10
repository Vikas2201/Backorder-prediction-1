# this module will predict the o./p

from Save_Model import save_methods
from application_logging.logging import logger_app
import pandas as pd
from data_perprocessing import preprocessing
import warnings

warnings.filterwarnings("ignore")

class prediction :
    def __init__(self):
        self.log_writer = logger_app()
        self.filepath ="Prediction_Logs/PredictionLog.txt"

    def convert_input_into_data(self,user_input):
        self.file_object = open(self.filepath , 'a')
        self.log_writer.log(self.file_object, 'Enter In Convert_input_into_data')
        self.input = user_input
        try:
            preprocessor = preprocessing.Preprocessor()
            df = pd.DataFrame(self.input, index=["forecast_3_month","forecast_6_month","forecast_9_month","sales_1_month","sales_3_month","sales_6_month","sales_9_month","perf_6_month_avg","perf_9_month_avg"])
            data = df.transpose()

            ##Convert categorical values to numeric values
            data = preprocessor.encode_categorical_columns(data)
            self.file_object.close()
            return data

        except Exception as error:
            self.log_writer.log(self.file_object, 'Error occured while running the convert_input_into_data!! Error:: %s' % error)
            self.file_object.close()
            raise error

    def get_prediction(self , data):
        # Logging the start of Prediction
        self.file_object = open(self.filepath , 'a')
        self.log_writer.log(self.file_object, 'Start of get_prediction')
        self.data = data
        try:
            model_loader = save_methods.Model_Operation()
            model_name = model_loader.find_correct_model_file()
            model = model_loader.load_model(model_name)
            result=list(model.predict(self.data))
            result = pd.DataFrame(result, columns=['Prediction'])
            result["Prediction"] = result["Prediction"].map({0: "Yes", 1: "No"})
            path = "Prediction_Output_File/Predictions.csv"
            result.to_csv("Prediction_Output_File/Predictions.csv", header=True,mode='a+')
            self.log_writer.log(self.file_object, 'End of get_prediction')
            self.file_object.close()

        except Exception as error:
            self.log_writer.log(self.file_object, 'Error occured while running the prediction!! Error:: %s' % error)
            self.file_object.close()
            raise error

