import configparser
import re
config = configparser.ConfigParser()
config.read('config/config.ini')
log_file = config.getboolean('logging', 'log_results_to_file')

def results(output):
    if log_file == True:
        resultfile = open("resultfile.txt", "a")
        clean_output = re.sub(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])', '', output)
        resultfile.write(f"{clean_output}\n")
        resultfile.close()
    else:
        return print(output)