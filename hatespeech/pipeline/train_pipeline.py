import sys
from hatespeech.logger import logging
from hatespeech.exception import CustomException
from hatespeech.components.data_ingestion import DataIngestion
#from hate.components.data_transforamation import DataTransformation
#from hate.components.model_trainer import ModelTrainer
#from hate.components.model_evaluation import ModelEvaluation
#from hate.components.model_pusher import ModelPusher

from hatespeech.entity.config_entity import (DataIngestionConfig,)

from hatespeech.entity.artifact_entity import (DataIngestionArtifacts,)


class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
    

    def start_data_ingestion(self) -> DataIngestionArtifacts:
        logging.info("Entered the start_data_ingestion method of TrainPipeline class")
        try:
            logging.info("Getting the data from s3 bucket")
            data_ingestion = DataIngestion(data_ingestion_config = self.data_ingestion_config)

            data_ingestion_artifacts = data_ingestion.initiate_data_ingestion()
            logging.info("Got the train and valid from s3")
            logging.info("Exited the start_data_ingestion method of TrainPipeline class")
            return data_ingestion_artifacts

        except Exception as e:
            raise CustomException(e, sys) from e
        
    

    def run_pipeline(self):
        logging.info("Entered the run_pipeline method of TrainPipeline class")
        try:
            data_ingestion_artifacts = self.start_data_ingestion()

            

            logging.info("Exited the run_pipeline method of TrainPipeline class") 

        except Exception as e:
            raise CustomException(e, sys) from e        