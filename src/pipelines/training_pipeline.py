from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

class TrainingPipeline:
    def __init__(self):
        pass
    def start_training(self):
        d=DataIngestion()
        dtf=DataTransformation()
        mt=ModelTrainer()
        train_path,test_path=d.initiate_data_ingestion()
        train_arr,test_arr,preprocessor_obj=dtf.initiate_data_transformation(train_path,test_path)
        best_model,best_score=mt.start_model_training(train_arr,test_arr)
        return best_model,best_score 
        
        