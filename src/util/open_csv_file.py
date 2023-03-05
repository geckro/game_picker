from csv import reader
from src.util.variables import *
def open_csv_file(file_path):
    data = []
    with open(file_path, "r", encoding=u8) as csv_file:
        csv_reader = reader(csv_file)
        for row in csv_reader:
            data.append(row)
    return data