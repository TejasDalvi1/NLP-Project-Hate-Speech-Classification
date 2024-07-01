from hatespeech.logger import logging
from hatespeech.exception import CustomException
import sys

#logging.info("Welcome")

try:
    1/0
except Exception as e:
    raise CustomException(e,sys)