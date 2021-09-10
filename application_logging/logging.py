
from datetime import datetime

class logger_app:
    def __init__(self):
        pass
    def log(self , file_object , log_massage):
        self.now = datetime.now()
        self.time  = self.now.strftime("%H:%M:%S")
        self.date = self.now.date()

        # write in file object
        # format "date/time  massage "
        file_object.write(
            "\n" + str(self.date) + "/" + str(self.time) + "\t\t" + log_massage + "\n"
        )