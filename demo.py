from hatespeech.logger import logging
from hatespeech.exception import CustomException
import sys
from hatespeech.configuration.gcloud_syncer import GCloudSync
#logging.info("Welcome")

obj=GCloudSync()
obj.sync_folder_from_gcloud("nlp_hatespeech","dataset.zip","download/dataset.zip")