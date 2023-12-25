import logging
import os
import datetime
current_time_stamp=f"{datetime.datetime.now().strftime('%d-%m-%Y_%H-%M-%S')}"
LOG_FILE_NAME=f"log_{current_time_stamp}.log"
LOG_DIR="diamond_logs"
os.makedirs(LOG_DIR,exist_ok=True)
LOG_FILE_PATH=os.path.join(LOG_DIR,LOG_FILE_NAME)

logging.basicConfig(filename=LOG_FILE_PATH,
                    level=logging.INFO,
                    
                    format="[%(asctime)s]-%(name)s-%(levelname)s:%(message)s ")
