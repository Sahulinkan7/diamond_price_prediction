from src.logger import logging 
from src.exception import CustomException
import os,sys 
from src.utils import load_object
import pandas as pd 


class Predictionpipeline:
    def __init__(self):
        pass
    def predict(self,features):
        try:
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            model_path=os.path.join('artifacts','model.pkl')
            
            logging.info("loading preprocessor and prediction model objects")
            prerocessor=load_object(preprocessor_path)
            model=load_object(model_path)
            
            data_scaled=prerocessor.transform(features)
            pred=model.predict(data_scaled)
            return pred
        
        except Exception as e:
            logging.info(f"Error in predictions")
            exc=CustomException(e,sys)
            logging.info(f"{exc.error_message}")
            
            
class CustomData:
    def __init__(self,carat:float,depth:float,table:float,x:float,y:float,z:float,cut:float,color:float,clarity:float):
        self.carat=carat
        self.depth=depth
        self.table=table 
        self.x=x
        self.y=y
        self.z=z
        self.cut=cut
        self.color=color
        self.clarity=clarity 
        
    def get_data_as_Dataframe(self):
        try:
            custom_data_input_dict={
                'carat':[self.carat],
                'depth':[self.depth],
                'table':[self.table],
                'x':[self.x],
                'y':[self.y],
                'z':[self.z],
                'cut':[self.cut],
                'color':[self.color],
                'clarity':[self.clarity]
            }
            df=pd.DataFrame(custom_data_input_dict)
            logging.info("Data Frame created")
            logging.info(f"{df.head(2).to_string()}")
            return df 
        except Exception as e:
            logging.info("error occurred while getting data as dataframe")
            exc=CustomException(e,sys)
            logging.info(f"{exc.error_message}")
            