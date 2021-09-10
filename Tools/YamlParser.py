import yaml
from yaml.loader import SafeLoader
from application_logging.logging import logger_app


class YamlParser:
    ''' this class helps us to read the Information from the Given Yaml FIles.    
    '''
    def __init__(self , yml_filePath ):
        self.yml_filePath = yml_filePath
        self.logger = logger_app()
        #self.logFilePath = 'D:\BackOrder_Intern\Training_Logs\yaml_parser.txt'
        self.logFilePath = 'Training_Logs\yaml_parser.txt'
    def yaml_parser(self):
        try:
            file_ = open(self.logFilePath , 'a+')
            self.logger.log(file_object= file_, log_massage=" Entered into : DBconnectionInfo-YamlParser..")
            with open(self.yml_filePath, 'r') as f:
                info = list(yaml.load_all(f, Loader=SafeLoader))
                f.close()
            self.logger.log( file_ , log_massage= f'File Parsed SuccessFully.. \n \t\t\t\t\t\t\t\t\t\t\t  {str(info)}')
            file_.close()
        except Exception as e:
            self.logger.log( file_ , log_massage=f'Exception : {str(e)}')
            file_.close()
            raise e
        return info
