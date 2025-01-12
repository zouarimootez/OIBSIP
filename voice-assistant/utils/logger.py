import logging
from datetime import datetime

def log(message):
    logging.basicConfig(filename="data/logs/app.log", level=logging.INFO)
    logging.info(f"{datetime.now()}: {message}")