import pandas as pd
import numpy as np
from dataclasses import dataclass
from src.logger import logging
from src.exception import CustomException
import os , sys
from sklearn.model_selection import train_test_split

@dataclass
class DataIngestionConfig:
    train_file_path=os.path.join("artifacts","train.csv")
    test_file_path=os.path.join("artifacts","test.csv")
    raw_file_path=os.path.join("artifacts","raw.csv")
    
class DataIngestion:
    def __init__(self):
        self.data_ingestion_config=DataIngestionConfig()
        
    def initiate_data_ingestion(self):
        logging.info(f"**************** Data Ingestion Started ****************")
        try:
            df=pd.read_csv(os.path.join("notebooks/data","gemstone.csv"))
            logging.info("dataset read as csv")
            
            os.makedirs(os.path.dirname(self.data_ingestion_config.raw_file_path),exist_ok=True)
            df.to_csv(self.data_ingestion_config.raw_file_path,index=False)
            logging.info(f"Data saved into {self.data_ingestion_config.raw_file_path} location ")
            
            logging.info(f"Splitting dataset into train and test dataset")
            
            train_df,test_df=train_test_split(df,test_size=0.20,random_state=44)
            train_df.to_csv(self.data_ingestion_config.train_file_path,index=False,header=True)
            test_df.to_csv(self.data_ingestion_config.test_file_path,index=False,header=True)
            
            logging.info(f"train file path is {self.data_ingestion_config.train_file_path}")
            logging.info(f"test file path is {self.data_ingestion_config.test_file_path}")
            logging.info(f"data ingestion completed ")
            
            return (self.data_ingestion_config.train_file_path,self.data_ingestion_config.test_file_path)
            
        except Exception as e:
            exc=CustomException(e,sys)
            logging.info(f"{exc.error_message}")