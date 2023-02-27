import os
import random

from src.logging_config import *

filename = os.path.basename(__file__)

def randomize_everything():
    with open("src/games.csv", "r", encoding="UTF8") as file:
        lines = file.readlines()
    random_line = random.choice(lines)
    column = random_line.split(",")

    bold = "\033[1m"
    red = "\033[31m"
    green = "\033[32m"
    orange = "\x1b[38;2;255;165;0m"
    reset = "\033[0m"

    game_title = f"{bold}{column[0]}{reset}"
    system = f"{red}{column[1]}{reset}" if column[1] else "NULL"
    date = f"{red}{column[2]}{reset}" if column[2] else "NULL"
    series = f"{red}{column[3]}{reset}" if column[3] else "NULL"
    version = f" {orange}{column[4]}{reset}" if column[4] else "NULL"
    developer = f" {orange}{column[7]}{reset}" if column[7] else "NULL"
    publisher = f" {orange}{column[8]}{reset}" if column[8] else "NULL"
    genre = f" {orange}{column[9]}{reset}" if column[9] else "NULL"
    print("-"*100)
    print("Title, System, Release Date, Series, Version, Developer, Publisher, Genre")
    print("-"*100)
    print(game_title, system, date, series, version, developer, publisher, genre)

def randomize_console():
    print("na")
def randomize_date():
    print("na")
def randomize_developer():
    print("na")

def randomize_games(selected_options_2):

    info_logger.info(f"File: |{filename}|")
    info_logger.info(f"Selected Options 2: |{selected_options_2}|")

    options = {
        "Randomize Everything": randomize_everything,
        "Randomize Console": randomize_console,
        "Randomize Date": randomize_date,
        "Randomize Developer": randomize_developer,
    }

    execute_list = options.get(selected_options_2, None)

    if execute_list is None:
        print("Error!")
    else:
        info_logger.info(f"Selected Option for Randomize: |{execute_list}|")
        execute_list()

# class random_line:
#     with open("./sources/games.csv", "r", encoding="utf8") as temp:
#     # Count amount of lines in the file
#         for filesize, line in enumerate(temp):
#                 pass
#     lines = filesize + 1
#     #print("INFO: Lines:",lines)
#     temp.close()
# class random_console:
#     from sys import argv
#     all = ["all", "everything"]
#     if argv[2] in all:
#         from random import choice
#         from lib.var_storage import consoleListSingular
#         tempConsole = []
#         for i in range(3):
#             random_choice = choice(consoleListSingular)
#             tempConsole.append(random_choice)
#         console = choice(tempConsole)
#     else:
#         console = argv[3].lower()
        
# class console_num:
#     from lib.var_storage import console_dictionary
#     console_num = console_dictionary[random_console.console]
# from lib.setting import log 
# log()
# from logging import debug
# def random_all():
#     class random_all:
#         from csv import reader
#         whileStop = 0
#         while whileStop != 1:

#             with open("./sources/games.csv", "r", encoding="UTF8") as temp2:
#                 # Prints a random number from the number set in the variable lines
#                 from random import randrange
#                 randomLine = randrange(random_line.lines)
#             temp2.close()

#             with open("./sources/games.csv", "r", encoding="UTF8") as games_csv:
#                 read_csv = reader(games_csv)
#                 for i in range(randomLine):
#                     next(read_csv)
#                 row = next(read_csv)

#                 # from the selected row, make console variable
#                 consoleRow = (row[1])
#                 # if the console variable matches the random console selected, exit while loop
#                 if console_num.console_num in consoleRow:
#                     whileStop = 1
#                     game = row[0]
#                     if row[2] != "":
#                         date = row[2]
#                     else:
#                         date = "NO DATE"
#                     if row[3] != "":
#                         series = row[3]
#                     else:
#                         series = "NULL"   
#                     break
#         print("Game Title     :       ",game)
#         print("Console        :       ",random_console.console)
#         print("Date           :       ",date)
#         print("Series         :       ",series)
# def random_sys():
#     class random_sys:
#         # Logging
#         from lib.setting import log
#         from csv import reader
#         from random import randrange
#         log()
#         whileStop = 0
#         while whileStop != 1:
#             with open("./sources/games.csv", "r", encoding="utf8") as temp2:
#                 # Prints a random number from the number set in the variable lines
#                 randomLine = randrange(random_line.lines)
#             temp2.close()

#             # Interacting with ./sources/games.csv

#             with open("./sources/games.csv", "r", encoding="utf8") as games_csv:
#                 read_csv = reader(games_csv)
#                 for i in range(randomLine):
#                     next(read_csv)
#                 row = next(read_csv)
#                 # from the selected row, make console variable
#                 consoleRow = (row[1])
                
#                 # if the console variable matches the random console selected, exit while loop
#                 if console_num.console_num in consoleRow:
#                     whileStop = 1
#                     n = row[0]
#                     break
#         if row[2] != "":
#             date1 = str(row[2])[:-2]
#             date2 = str(row[2])[-2:]
#             date = date1+"-"+date2
#         else:
#             date = "NULL"
#         if row[3] != "":
#             series = row[3]
#         else:
#             series = "NULL"    
#         print("Game Title     :       ",n)
#         print("Series         :       ",series)
#         print("Date           :       ",date)