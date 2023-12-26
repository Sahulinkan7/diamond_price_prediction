from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler,OrdinalEncoder
from sklearn.pipeline import Pipeline
import pandas as pd
import os,sys
from dataclasses import dataclass
from src.logger import logging
from src.exception import CustomException
import numpy as np
from src.utils import save_object
## Data Transformation Config
@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join("artifacts","preprocessor.pkl")

## Data Transformation Class
class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()
        
    def get_transformation_object(self):
        try:
            logging.info(f"********************* Data Transformation initiated **********************")
            categorical_cols=['cut','color','clarity']
            numerical_cols=['carat','depth','table','x','y','z']
            
            # custom ranking for each ordinal variable
            cut_categories=['Fair','Good','Very Good','Premium','Ideal']
            color_categories=['D','E','F','G','H','I','J']
            clarity_categories=['I1','SI2','SI1','VS2','VS1','VVS2','VVS1','IF']
            
            num_pipeline=Pipeline(
                steps=[
                    ('imputer',SimpleImputer(strategy='median')),
                    ('scaler',StandardScaler())
                ]
            )
            
            # categorical pipeline
            cat_pipeline=Pipeline(
                steps=[
                    ('imputer',SimpleImputer(strategy='most_frequent')),
                    ('ordinalencoder',OrdinalEncoder(categories=[cut_categories,color_categories,clarity_categories])),
                    ('scaler',StandardScaler())
                ]
            )
            
            preprocessor=ColumnTransformer([
                ('num_pipeline',num_pipeline,numerical_cols),
                ('cat_pipeline',cat_pipeline,categorical_cols),
            ])
            
            logging.info(f"feature engineering completed !")
            return preprocessor
        
        except Exception as e:
            transformexc=CustomException(e,sys)
            logging.info(f"{transformexc.error_message}")
    
    def initiate_data_transformation(self,train_data_path,test_data_path):
        try:
            logging.info(f"********************* Data Transformation initiated **********************")
            logging.info(f"reading train and test data ")
            train_df=pd.read_csv(train_data_path)
            test_df=pd.read_csv(test_data_path)
            
            logging.info(f"train data is \n{train_df.head().to_string()}")
            logging.info(f"test dataframe is \n{test_df.head().to_string()}")
            
            logging.info('Obtaining preprocessing object')
            
            preprocessing_object=self.get_transformation_object()
            
            target_column_name='price'
            drop_columns=[target_column_name,'id']
            
            input_feature_train_df=train_df.drop(columns=drop_columns,axis=1)
            target_feature_train_df=train_df[target_column_name]

            input_feature_test_df=test_df.drop(columns=drop_columns,axis=1) 
            target_feature_test_df=test_df[target_column_name]
            
            ## applying the transformation
            input_feature_train_arr=preprocessing_object.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessing_object.transform(input_feature_test_df)
            
            logging.info("applying preprocessing object on train and test dataframe to get the final train and test array")
            train_arr=np.c_[input_feature_train_arr,np.array(target_feature_train_df)]
            test_arr=np.c_[input_feature_test_arr,np.array(target_feature_test_df)]
            
            save_object(file_path=self.data_transformation_config.preprocessor_obj_file_path,
                        obj=preprocessing_object)
            logging.info('preprocessor object file created and saved')
            
            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path
            )
        except Exception as e:
            exc=CustomException(e,sys)
            logging.info(f"error occurred during data transformation")
            logging.info(f"{exc.error_message}")