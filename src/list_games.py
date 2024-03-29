try:
    import configparser
    from datetime import datetime
    from src.logging_config import *
    from src.util.date_extract import date_extraction
    from src.util.open_csv_file import open_csv_file
    from src.util.output import print_output
    from src.util.results import results
    from src.util.system_dictionary import *
    from src.util.variables import *
except ModuleNotFoundError as ERR:
    error_logger.error(f"Failed to import {ERR.name} module: {ERR}")

def dev_check(dev):
    # TODO: is there a faster way instead of using a list variable?
    developers = []
    read_csv = open_csv_file(csv)
    for column in read_csv:
        if column[7] not in developers:
            developers.append(column[7])
    developers.sort()
    if dev in developers:
        return True
    else:
        return False

def list_everything():
    # opens games.csv as var games_csv
    read_csv = open_csv_file(csv)

    for column in read_csv:
        # Extract the date and if date includes "-" strip it out
        date_str = date_extraction(column[2])
        # Print output
        output = print_output(column, date_str, "null")
        results(output)
    # For proper formatting
    print()

def list_developer():
    # Makes user input a developer and checks to see if that user is in the csv developer column. If developer not in column, it asks again.
    while True:
        developer = input("Enter developer: ")
        check_developer = dev_check(developer)
        print(check_developer)
        if check_developer == True:
            break
        elif check_developer == False:
            print(f"{developer} does not exist!")
    info_logger.info(f"Developer: |{developer}|")
    # List all entries of specified developer in games.csv
    read_csv = open_csv_file(csv)
    print(f"\nGames developed by {developer}:\n")
    for column in read_csv:
        date_str = date_extraction(column[2])
        # Print the formatted output
        if developer.lower() in column[7].lower():
            output = print_output(column, date_str, "no_developer")
            results(output)
    print()

def list_steam():
    # Lists all games that are on steam or was on steam.
    read_csv = open_csv_file(csv)
    print(f"\nGames that are on Steam:\n")
    for column in read_csv:
        date_str = date_extraction(column[2])
        # Print the formatted output
        if column[11] != "":
            output = print_output(column, date_str, "null")
            results(output)
    print()

# List all entries of chosen console in games.csv
def list_system():
    system_input = input("Enter system: ").lower()
    if system_input in sys_dict:
        system = sys_dict[system_input]
    read_csv = open_csv_file(csv)
    info_logger.info(f"System: |{system}|")
    info_logger.info(f"System Input: |{system_input}|")

    config = configparser.ConfigParser()
    config.read('config/config.ini')
    log_file = config.getboolean('logging', 'log_results_to_file')

    if log_file:
        print("Printing results to [resultfile.txt]")
    else:
        print(f"\nGames that released on {system_input}:\n")

    for column in read_csv:
        date_str = date_extraction(column[2])
        # Print the formatted output
        if column[1].lower() == system.lower():
            output = print_output(column, date_str, "no_system")
            results(output)
    print()

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


    def date_enter():

        date = input("Enter date: ")

        info_logger.info(f"Date 1: |{date}|")
        for char in "/\\, .-":
            date = date.replace(char, "")
        info_logger.info(f"Date 1 (Replaced): |{date}|")

        while not is_valid_date(date):
            print("Invalid date format. Please try again.")

            date = input("Enter date: ")

            info_logger.info(f"Date 2: |{date}|")
            for char in "/\\, .-":
                date = date.replace(char, "")
            info_logger.info(f"Date 2 (Replaced): |{date}|")

        info_logger.info(f"Length of Date: |{len(date)}|")

        return date

    # List all entries of specified release date in games.csv
    read_csv = open_csv_file(csv)
    length_dict = {4:4, 6:6, 8:8}
    date = date_enter()
    length = len(date)
    if length in length_dict:
        info_logger.info(f"Chose {length} length")

        config = configparser.ConfigParser()
        config.read('config/config.ini')
        title_value = config.getboolean('sorting', 'sort_title')
        date_value = config.getboolean('sorting', 'sort_date')

        # Sort by Title
        if title_value == True:
            for column in read_csv:
                
                date_str = date_extraction(column[2])

                # Print the formatted output
                if date in column[2][:length_dict[length]]:
                    output = print_output(column, date_str, "null")
                    results(output)
            print()

        # Sort by Date

        # elif date_value == True:

        #     # Create a temporary empty list to store the following entries
        #     entries = []

        #     # Loop through each row in the CSV file
        #     for row in read_csv:
        #         # Extract the date from the row
        #         row_date_str = row[2]

        #         # If the row's date matches the input date
        #         if date in row_date_str:
        #             date_str = format_date(row[2])

        #             # Store the entry in the list
        #             entries.append((date_str, row[0], row[1], row[4]))

        #     # Sort the entries by date
        #     entries.sort()

        #     # Print the sorted entries
        #     for entry in entries:
        #         game_title = f"{bold}{row[0]}{reset}"
        #         console_name = f"{red}{row[1]}{reset}" 
        #         date_str = f"{green}{date_str}{reset}"
        #         version = f"{orange}{row[4]}{reset}" if row[4] else ""
        #         date_str, game_title, console_name, version = entry
                

        #         print("{:<{width}}{:<20}{:<15}{}".format(game_title, console_name, date_str, version, width=max_title_length))

        #     # Print a blank line after the output
        #     print("")

def list_games(selected_options_2):
    info_logger.info(f"File: |{filename}|")
    info_logger.info(f"Selected Options 2: |{selected_options_2}|")
    options = {
        "List Everything": list_everything,
        "List Console": list_system,
        "List Date": list_date,
        "List Developer": list_developer,
        "List Games on Steam": list_steam,
    }
    execute_list = options.get(selected_options_2, None)
    if execute_list is None:
        print("Error!")
    else:
        info_logger.info(f"Selected Option for List: |{execute_list}|")
        execute_list()
if __name__ == "__main__":
    print("YOU CANNOT RUN THIS FILE DIRECTLY!\nexiting...")
    exit()