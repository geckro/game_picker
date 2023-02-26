import logging
import os

from datetime import datetime
from csv import reader
from InquirerPy import inquirer
from InquirerPy.base import Choice
from InquirerPy.separator import Separator

filename = os.path.basename(__file__)

def list_everything():
    
    with open("src/games.csv", "r", encoding="UTF8") as games_csv:
        read_csv = reader(games_csv)
        for column in read_csv:
            # Extract the year, month, and day from column[2]
            year = column[2][:4]
            month = column[2][4:6]
            day = column[2][6:8]

            # Create a formatted string for the date with hyphens
            date_str = f"{year}-{month}-{day}"

            # Set the color codes for the console output
            bold = "\033[1m"
            red = "\033[31m"
            green = "\033[32m"
            reset = "\033[0m"

            # Print the formatted output
            game_title = f"{bold}{column[0]}{reset}"
            console_name = f"{red}{column[1]}{reset}"
            date_str = f"{green}{date_str}{reset}"

            print(f"{game_title}, {console_name}, {date_str}")
        print("")

def list_developer():

    developer = input("Enter developer: ")

    logging.info(f"Developer: |{developer}|")

    # List all entries of specified developer in games.csv
    with open("src/games.csv", "r", encoding="UTF8") as games_csv:
        read_csv = reader(games_csv)
        print(f"\nGames developed by {developer}:\n")
        for column in read_csv:
            # Extract the year, month, and day from column[2]
            year = column[2][:4]
            month = column[2][4:6]
            day = column[2][6:8]

            # Create a formatted string for the date with hyphens
            date_str = f"{year}-{month}-{day}"

            # Set the color codes for the console output
            bold = "\033[1m"
            red = "\033[31m"
            green = "\033[32m"
            reset = "\033[0m"

            # Print the formatted output
            if developer.lower() in column[7].lower():

                game_title = f"{bold}{column[0]}{reset}"
                console_name = f"{red}{column[1]}{reset}"
                date_str = f"{green}{date_str}{reset}"

                print(f"{game_title}, {console_name}, {date_str}")
        print("")

def list_console():
    # List all entries of chosen console in games.csv

    def systems(_):
        return [
            "Microsoft - Windows",
            "Microsoft - Xbox",
            "Microsoft - Xbox 360",
            "Microsoft - Xbox One",
            "Microsoft - Xbox Series X/S",
            "Microsoft - Xbox Live Arcade",
            "Nintendo - 3DS",
            "Nintendo - DS",
            "Nintendo - DSiWare",
            "Nintendo - Game Boy",
            "Nintendo - Game Boy Color",
            "Nintendo - Game Boy Advance",
            "Nintendo - GameCube"
            "Nintendo - NES / Famicom",
            "Nintendo - Nintendo 64",
            "Nintendo - Super Nintendo",
            "Nintendo - Switch",
            "Nintendo - Virtual Boy",
            "Nintendo - Wii",
            "Nintendo - WiiWare",
            "Nintendo - Wii U",
            "Philips - CD-i",
            "Sega - 32X",
            "Sega - Dreamcast",
            "Sega - Genesis / Mega Drive",
            "Sega - Master System",
            "Sega - Sega CD",
            "Sega - Saturn",
            "Sony - PlayStation 1",
            "Sony - PlayStation 2",
            "Sony - PlayStation 3",
            "Sony - PlayStation 4",
            "Sony - PlayStation 5",
            "Sony - PlayStation Network",
            "Sony - PlayStation Portable",
            "Sony - PlayStation Vita",
        ]
    system_checkbox = inquirer.checkbox(
        message="Pick one or more systems:",
        choices=systems,
        validate=lambda result: len(result) >= 1,
        invalid_message="should be at least 1 selection",
        instruction="(select at least 1)",
    ).execute()
    
    # Log the selected option for the first select inquiry.
    logging.info(f'Selected Systems: |{system_checkbox}|')
    
    # with open("src/games.csv", "r", encoding="UTF8") as games_csv:
    #     read_csv = reader(games_csv)
    #     print("List of",console_num.consoleName,"games")
    #     print("DATE      |      NAME      |      SERIES")
    
    #     # TODO: Make function print multiple lines
    #     # If sort date is wanted, write the results to a file, sort it alphabetically, and then print results.
    #     if console_num.date_var == 1:
    #         temp = open('temp.txt', 'w')
    #         temp.close()    
    #         for column in read_csv:
    #             if console_num.consoleNum in column[1]:
    #                 temp = open('temp.txt', 'a')
    #                 temporary = column[2],column[0]
    #                 temp.write(str(temporary) + "\n")
    #                 temp.close()
    #         with open("temp.txt", "r+") as file:
    #                 temp2 = sorted(file.readlines())
                
    #                 file.write(str(temp2))
    
    #     #  If sort date is not wanted, just list from the csv file.
    #     for column in read_csv:
    #             if console_num.consoleNum in column[1]:
    #                 print(column[2],"|",column[0],"|",column[3])

    print("na")

def list_date():

    def is_valid_date(date_str: str) -> bool:
        
        allowed_date_formats = ["%Y%m%d", "%Y%m", "%Y"]

        for date_format in allowed_date_formats:
            try:
                datetime.strptime(date_str, date_format)
                return True
            except ValueError:
                pass
        return False


    date = input("Enter date: ")

    logging.info(f"Date 1: |{date}|")
    for char in "/\\, .-":
        date = date.replace(char, "")
    logging.info(f"Date 1 (Replaced): |{date}|")

    while not is_valid_date(date):
        print("Invalid date format. Please try again.")

        date = input("Enter date: ")

        logging.info(f"Date 2: |{date}|")
        for char in "/\\, .-":
            date = date.replace(char, "")
        logging.info(f"Date 2 (Replaced): |{date}|")

    logging.info(f"Length of Date: |{len(date)}|")

    # List all entries of specified release date in games.csv
    with open("src/games.csv", "r", encoding="UTF8") as games_csv:
        read_csv = reader(games_csv)
        length_dict = {4:4, 6:6, 8:8}
        length = len(date)
        if length in length_dict:
            logging.info(f"Chose {length} length")
            for column in read_csv:
                # Extract the year, month, and day from column[2]
                year = column[2][:4]
                month = column[2][4:6]
                day = column[2][6:8]

                # Create a formatted string for the date with hyphens
                date_str = f"{year}-{month}-{day}"

                # Set the color codes for the console output
                bold = "\033[1m"
                red = "\033[31m"
                green = "\033[32m"
                reset = "\033[0m"

                # Print the formatted output
                if date in column[2][:length_dict[length]]:

                    game_title = f"{bold}{column[0]}{reset}"
                    console_name = f"{red}{column[1]}{reset}"
                    date_str = f"{green}{date_str}{reset}"

                    print(f"{game_title}, {console_name}, {date_str}")
            print("")

def list_games(selected_options_2):

    logging.info(f"File: |{filename}|")
    logging.info(f"Selected Options 2: |{selected_options_2}|")

    options = {
        "List Everything": list_everything,
        "List Console": list_console,
        "List Date": list_date,
        "List Developer": list_developer,
    }

    execute_list = options.get(selected_options_2, None)

    if execute_list is None:
        print("Error!")
    else:
        logging.info(f"Selected Option for List: |{execute_list}|")
        execute_list()