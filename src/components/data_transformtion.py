# To transform the input data such as one hot encoding, etc.

import sys
from dataclasses import dataclass
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from src.exception import CustomException
from src.logger import logging
import os
from src.utils import save_object

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifact',"preprocessor.pkl")

class DataTransformation:

    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()

    # This function is responsible for data tranformation
    def get_data_transformer_object(self):
        try:
            numerical_columns = [
                'writing_score',
                'reading_score'
            ]
            categorical_columns = [
                'gender',
                'race_ethnicity',
                'parental_level_of_education',
                'lunch',
                'test_preparation_course'
            ]
            num_pipeline=Pipeline(
                steps=[
                    # To handle the missing values
                    ('imputer',SimpleImputer(strategy='median')),
                    # To scale the data
                    ('scaler',StandardScaler())
                ]
            )
            cat_pipeline=Pipeline(
                steps=[
                    # Applying mode for missing values
                    ('imputer',SimpleImputer(strategy='most_frequent')),
                    # Converting categorical to numerical features
                    ('one_hot_encoder',OneHotEncoder()),
                    # Scaling the data
                    ('scaler',StandardScaler(with_mean=False))
                ]
            )
            logging.info(f'Categorical columns: {categorical_columns}')
            logging.info(f'Numerical columns: {numerical_columns}')
            # Combining the numerical and categorical pipelines
            preprocessor=ColumnTransformer(
                [
                    ('num_pipeline',num_pipeline,numerical_columns),
                    ('cat_pipeline',cat_pipeline,categorical_columns)
                ]
            )
            return preprocessor
        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_data_tranformation(self,train_path,test_path):
        try:
            # Reading the train and test dataset generated from data ingestion
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)
            # Logging the info
            logging.info('Read train and test data completed')
            logging.info('Obtaining preprocessing object')
            # Using preprocessing object from above class to transform data
            preprocessing_obj=self.get_data_transformer_object()
            # Identifying type of feature
            target_column_name='math_score'
            numerical_columns = [
                'writing_score',
                'reading_score'
            ]
            # Defining training input and output
            input_feature_train_df=train_df.drop(columns=[target_column_name],axis=1)
            target_feature_train_df=train_df[target_column_name]
            # Defining testing input and output
            input_feature_test_df=test_df.drop(columns=[target_column_name],axis=1)
            target_feature_test_df=test_df[target_column_name]
            # logging info
            logging.info('Applying preprocessing object on training dataframe and testing dataframe.')
            # applying transformation on the training dataset
            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)
            '''np.c_[np.array([1,2,3]), np.array([4,5,6])]
                array([[1, 4],
                    [2, 5],
                    [3, 6]])'''
            train_arr = np.c_[
                input_feature_train_arr, np.array(target_feature_train_df)
            ]
            test_arr = np.c_[
                input_feature_test_arr, np.array(target_feature_test_df)
            ]
            # logging the preprocessing task
            logging.info('Saved preprocessing object.')
            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj
            )
            return(
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,
            )
        except Exception as e:
            raise CustomException(e,sys)