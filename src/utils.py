from src.logger import logging 
from src.exception import CustomException
import os,sys,pickle
from sklearn.metrics import r2_score
def save_object(file_path,obj):
    try:
        dir_path=os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        with open(file_path,"wb") as file_obj:
            pickle.dump(obj,file_obj)
    except Exception as e:
        logging.info("Error while saving pickle file")
        ex=CustomException(e,sys)
        logging.info(ex.error_message)
        
def evaluate_model(x_train,y_train,x_test,y_test,models:dict):
    try:
        reports={}
        for i in range(len(models)):
            model=list(models.values())[i]
            
            logging.info(f" Model Training started for model : {model}")
            model.fit(x_train,y_train)
            logging.info(f"Model Training ended for model : {model}")
            
            y_test_predict=model.predict(x_test)
            
            test_model_score=r2_score(y_test,y_test_predict)
            
            reports[list(models.keys())[i]] = test_model_score
        return reports
            
    except Exception as e:
        exc=CustomException(e,sys)
        logging.error(f"Exception occured during model Evaluation")
        logging.info(f"{exc.error_message}")
        
        
def load_object(file_path):
    try:
        with open(file_path,"rb") as file_obj:
            return pickle.load(file_obj)
    except Exception as e:
        logging.info(f"Exception occurred in load object function utils")
        exc=CustomException(e,sys)
        logging.info(f"{exc.error_message}")