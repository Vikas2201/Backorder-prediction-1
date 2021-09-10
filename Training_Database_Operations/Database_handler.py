# this file helps to create the Good_training_tables

from cassandra.query import dict_factory
from application_logging.logging import logger_app
from Tools.DBconnector import DBconnector
from Tools.YamlParser import YamlParser
import csv 
import os
import pandas as pd


class Database_Operations:
    def __init__(self):
        self.goodfilepath = "Training_Raw_files_validated/Good_Raw"
        self.yaml_path = "Controllers/DBconnection_info.yaml"
        self.logger = logger_app()
        self.session = DBconnector().connect()
        self.key_space = YamlParser(self.yaml_path).yaml_parser()[0]['Good_training_tables_info']['keyspace_name']
        self.Good_training_TableName = YamlParser(self.yaml_path).yaml_parser()[0]['Good_training_tables_info']['table_name']

    def CreateGoodTraining_table(self):
        ''' Task : this method will create the GoodTraining Table to store the Validated data.
            Inputs : Receives the Inputs from "DBconnection_info.yaml" files
            Ip/1 : database connector pointer
            Ip/2 : Good-Training-TableName 
            Ip/3 : perticular keyspace 
            return : None 
            by : shubham chau
        '''
        try : 
            self.f_ = open('Training_logs/TrainingDatabseInfo.txt' , 'a')
            self.logger.log( self.f_ , 'Entered into the class : CreateGoodTraining_table ....' )
            self.session.execute(f"use {self.key_space}")
            self.session.execute(f"CREATE TABLE if not exists {self.Good_training_TableName} ( sku  int PRIMARY KEY,,national_inv  float , lead_time  float , in_transit_qty  float , forecast_3_month  float , forecast_6_month  float , forecast_9_month  float , sales_1_month  float , sales_3_month  float ,sales_6_month  float , sales_9_month  float ,min_bank  float , potential_issue  text,pieces_past_due  float , perf_6_month_avg  float , perf_12_month_avg  float , local_bo_qty  float ,deck_risk  text,oe_constraint  text  , ppap_risk  text,stop_auto_buy  text,rev_stop  text,went_on_backorder  text) ;" )
            self.logger.log(self.f_ , f"{self.Good_training_TableName }  created Successfully !...." )
            self.f_.close()
        except Exception as e :
            self.logger.log(file_object= self.f_ , log_massage= "Excepation : " + str(e))
            self.f_.close()
            raise e 

    def DataInsertion(self):
        '''
                Method Name: DataInsertion
                Description: This method inserts the Good data files from the Good_Raw folder into the
                            above created table.
                Output: None
                On Failure: Raise Exception
                by : shubham chau.

        '''
        
        goodfilepath = self.goodfilepath        
        log_f = open("Training_Logs/DataImportExport.txt" , 'a')
        self.logger.log(log_f , 'Entered Into Class : DataBaseOperations > DataInsertion ')
        self.logger.log(log_f , f'Files found in Good Raw dirs  :{str (os.listdir(self.goodfilepath) ) }')

        try : 
            self.session.execute(f"use {self.key_space}" )
            files = [file_ for file_ in os.listdir(self.goodfilepath)]
            for file_ in files :
                f_path = os.path.join(goodfilepath , file_)
                # pandas operations
                data = pd.read_csv(f_path)
                a = data.values
                try :
                    for record in a :
                        l = list(record)
                        Query_2 = f"Insert into {self.Good_training_TableName} (sku,national_inv,lead_time,in_transit_qty,forecast_3_month,forecast_6_month,forecast_9_month,sales_1_month,sales_3_month,sales_6_month,sales_9_month,min_bank,potential_issue,pieces_past_due,perf_6_month_avg,perf_12_month_avg,local_bo_qty,deck_risk,oe_constraint,ppap_risk,stop_auto_buy,rev_stop,went_on_backorder) values ({l[0]} , {l[1]} ,  {l[2]} ,  {l[3]} , {l[4]}  ,  {l[5]} ,  {l[6]} ,  {l[7]} , {l[8]} , {l[9]}  ,  {l[10]} , {l[11]} ,  '{l[12]}' , {l[13]} , {l[14]} ,  {l[15]}  ,  {l[16]},  '{l[17]}',  '{l[18]}' ,  '{l[19]}',  '{l[20]}',  '{l[21]}' ,  '{l[22]}');"
                        self.session.execute(Query_2)

                    self.logger.log(log_f , log_massage= "Data Uploaded successfully ...." )
                    log_f.close()

                except Exception as e :
                    self.logger.log(log_f , 'Exception Occures in Data Insertion PRocess  ... . ')
                    self.logger.log(log_f, 'Exception ' + str(e))
                    raise e

        except Exception as e :            
            self.logger.log(file_object=log_f , log_massage= 'Exception : ' + str(e))
            log_f.close() 
            raise e 

    def DataImport(self):
        '''
                MEthodName : DataImport 
                Task : This  method will Import the Data from  Table & convert / store this data into the Csv Format .
                Opfilelocation : 'Training_FileFromDB/'
                return : None
                by : shubham chau         
        
        '''
        self.fileFromDb = 'Training_FileFromDB/'
        self.fileName = 'InputFile.csv'   # the file Inwhich datawill be storing 
        log_f = open("Training_Logs/DataImportExport.txt" , 'a')  # Log File to Capture Process 
        self.logger.log(log_f , 'Entered Into Class : DataBaseOperations > DataImport ')

        # creating the Dir to store the Data
        if not os.path.isdir(self.fileFromDb):
            os.makedirs(self.fileFromDb)        

        try :
            self.session.execute(f"use {self.key_space}" )
            Query = f"select * from {self.Good_training_TableName} ;"
            self.session.row_factory = dict_factory
            rows = list(self.session.execute(Query) )  
            # storing the data into csv file 
            try :
                fieldnames = [   'sku','national_inv', 'lead_time', 'in_transit_qty', 'forecast_3_month',
                                'forecast_6_month', 'forecast_9_month', 'sales_1_month',
                                'sales_3_month', 'sales_6_month', 'sales_9_month', 'min_bank',
                                'potential_issue', 'pieces_past_due', 'perf_6_month_avg',
                                'perf_12_month_avg', 'local_bo_qty', 'deck_risk', 'oe_constraint' , 
                                'ppap_risk', 'stop_auto_buy', 'rev_stop', 'went_on_backorder'
                                ]
                with open(self.fileFromDb + self.fileName , mode='w' , newline="") as csv_file :
                    writer = csv.DictWriter( csv_file , fieldnames= fieldnames)
                    writer.writeheader()
                    writer.writerows(rows) 

                self.logger.log(file_object=log_f , log_massage= f" Data Imported in to file {os.path.join(self.fileFromDb , self.fileName)}")
                log_f.close()

            except Exception as e :
                self.logger.log(log_f , log_massage= "Exeption : Method : DataImport => " + str(e))
                log_f.close()
                raise e
                
        except Exception as e :
                self.logger.log(log_f , log_massage= "Exeption : Method : DataImport => " + str(e))
                log_f.close()
                raise e 

        
        


            
        







    

        

         













