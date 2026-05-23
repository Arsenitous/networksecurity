from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import CustomException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import TrainingPipelineConfig

from networksecurity.entity.config_entity import DataIngestionConfig

import sys

if __name__ == "__main__":
    try:
        training_pipeline_config = TrainingPipelineConfig()
        logging.info("Staring data ingestion")
        data_ingestion_config = DataIngestionConfig(training_pipeline_config)
        data_ingestion = DataIngestion(data_ingestion_config)
        dataingestion_artifact = data_ingestion.initiate_data_ingestion()
        logging.info("Data ingestion completed")
        print(dataingestion_artifact)

        # logging.info("Starting data validation")
        # data_validation_config = DataValidationConfig(training_pipeline_config)
        # data_validation = DataValidation(data_validation_config)
        # data_validation_artifact = data_validation.initiate_data_validation()
        # logging.info("Data validation completed")
        # print(data_validation_artifact)

        # logging.info("Starting data transformation")
        # data_transformation_config = DataTransformationConfig(training_pipeline_config)
        # data_transformation = DataTransformation(data_transformation_config)
        # data_transformation_artifact = data_transformation.initiate_data_transformation()
        # logging.info("Data transformation completed")
        # print(data_transformation_artifact)

        # logging.info("Starting model training")
        # model_trainer_config = ModelTrainerConfig(training_pipeline_config)
        # model_trainer = ModelTrainer(model_trainer_config)
        # model_trainer_artifact = model_trainer.initiate_model_training()
        # logging.info("Model training completed")
        # print(model_trainer_artifact)

    except Exception as e:
        logging.info(e)
        raise CustomException(e, sys)
