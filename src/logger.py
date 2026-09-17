import logging
import os
from datetime import datetime

#creating and defining naming convention for the log file
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
#creating logs folder and defining its location in current directory
logs_path = os.path.join(os.getcwd(), "logs")
#avoiding error if logs folder already exists
os.makedirs(logs_path, exist_ok=True)
#directing LOG_FILE into the logs folder
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

#Create template for the log message to be saved into log file
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format= "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level= logging.INFO
)


