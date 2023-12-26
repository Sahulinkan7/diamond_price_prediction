from src.logger import logging 
from src.exception import CustomException
import os,sys,pickle
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