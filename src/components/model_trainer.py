from dataclasses import dataclass
from src.exception import CustomException
from src.logger import logging
from sklearn.linear_model import LinearRegression,Ridge,Lasso,ElasticNet
import os,sys 
from src.utils import evaluate_model
from src.utils import save_object
@dataclass
class ModelTrainerConfig:
    trained_model_path=os.path.join("artifacts","model.pkl")
    
    
class ModelTrainer:
    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig()
        
    def start_model_training(self,train_arr,test_arr):
        try:
            logging.info(f"****************** Model Training Started ********************")
            logging.info(f"Splitting dependent and independent variables from trainer and test data")
            x_train,y_train,x_test,y_test=(train_arr[:,:-1],train_arr[:,-1],test_arr[:,:-1],test_arr[:,-1])
            models={
                'LinearRegression':LinearRegression(),
                'Ridge':Ridge(),
                'Lasso':Lasso(),
                'Elasticnet':ElasticNet()                
            }
            
            model_reports:dict=evaluate_model(x_train,y_train,x_test,y_test,models)
            logging.info(f"Model Report \n {model_reports}")
            
            best_model_score=max(sorted(list(model_reports.values())))
            
            best_model_name=list(model_reports.keys())[list(model_reports.values()).index(best_model_score)]
            
            best_model=models[best_model_name]
            
            logging.info(f"Best model found , Model name : {best_model_name} and its R2_Score is {best_model_score}")
            save_object(file_path=self.model_trainer_config.trained_model_path,obj=best_model)
            logging.info(f"Best model object saved after model training")
            logging.info("****************** Model Training Ended ********************")
            return (
                best_model_name, best_model_score
            )
        except Exception as e:
            logging.info("Error occurred during model training")
            exc=CustomException(e,sys)
            logging.error(f"{exc.error_message}")