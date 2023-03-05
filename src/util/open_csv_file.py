from csv import reader
from src.util.variables import *
from src.logging_config import *
def open_csv_file(file_path):
    try:
        with open(file_path, "r", encoding=u8) as csv_file:
            return [row for row in reader(csv_file)]
    except FileNotFoundError or Exception:
        error_logger.error(f"Could not find games.csv file: {file_path}")