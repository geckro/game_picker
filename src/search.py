try:
    from src.util.open_csv_file import open_csv_file
    from src.util.variables import *
    from src.logging_config import *
    from src.util.date_extract import date_extraction
    from src.util.output import print_output
    from src.util.results import results
except ModuleNotFoundError as ERR:
    error_logger.error(f"Failed to import {ERR.name} module: {ERR}")

def search_csv():
    search_input = input("Enter search: ")
    read_csv = open_csv_file(csv)
    for column in read_csv:
        if search_input.lower() in column[0].lower():
            date_str = date_extraction(column[2])
            output = print_output(column, date_str, "null")
            results(output)