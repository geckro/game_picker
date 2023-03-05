import logging
from logging.handlers import RotatingFileHandler

from os import mkdir
from os.path import exists, join

# Create the logs directory if it does not exist
logs_dir = "logs"
if not exists(logs_dir):
    mkdir(logs_dir)

# Set up logger for INFO level
info_logger = logging.getLogger("info_logger")
info_logger.setLevel(logging.INFO)
info_formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s")
info_handler = RotatingFileHandler(
    join(logs_dir, "info.log"), maxBytes=1024 * 1024, backupCount=1
)
info_handler.setFormatter(info_formatter)
info_logger.addHandler(info_handler)

# Set up logger for ERROR level
error_logger = logging.getLogger("error_logger")
error_logger.setLevel(logging.ERROR)
error_formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s")
error_handler = RotatingFileHandler(
    join(logs_dir, "error.log"), maxBytes=1024 * 1024, backupCount=1
)
error_handler.setFormatter(error_formatter)
error_logger.addHandler(error_handler)
