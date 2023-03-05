import configparser
import re

config = configparser.ConfigParser()
config.read('config/config.ini')
log_file = config.getboolean('logging', 'log_results_to_file')

def results(output):
    if log_file:
        try:
            with open("resultfile.txt", "a") as resultfile:
                clean_output = re.sub(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])', '', output)
                resultfile.write(f"{clean_output}\n")
        except IOError as results_error:
            print(f"Error writing to resultfile.txt: {results_error}")
    else:
        return print(output)