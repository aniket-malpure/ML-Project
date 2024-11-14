# To log the changes

import logging
import os
from datetime import datetime

# file name format
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%M_%S')}.log"

# log file path
logs_path=os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(logs_path,exist_ok=True)
LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

# To overwrite the logging functionality update the basic config
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)