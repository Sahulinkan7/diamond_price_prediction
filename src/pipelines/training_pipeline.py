from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation

class TrainingPipeline:
    def __init__(self):
        pass
    def start_training(self):
        d=DataIngestion()
        dtf=DataTransformation()
        train_path,test_path=d.initiate_data_ingestion()
        train_arr,test_arr,preprocessor_obj=dtf.initiate_data_transformation(train_path,test_path)
        
        
t=TrainingPipeline()
t.start_training()
        