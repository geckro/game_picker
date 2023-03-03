import configparser

from InquirerPy import inquirer
from InquirerPy.base import Choice
from InquirerPy.separator import Separator
from src.logging_config import *
from sys import exit

# First key gets asked at "option" variable. Second key gets asked at "option_select" variable
config_options = {
    # 1st key
    "Sort Settings": [
        # 2nd key
        "Sort by Title",
        "Sort by Date",
    ],
    # 1st key
    "Logging Settings": [
        # 2nd key
        "Log All",
        "Log Errors",
        "Log Nothing",
    ],
    "Steam Settings": [
        "Show URLs",
        "Dont Show URLs",
    ],

}

def configure_settings():
    
    # Asks the what config they want to configure
    option = inquirer.select(
        message="Select configuration:",
        choices=list(config_options.keys()),
        default=1,
    ).execute()

    info_logger.info(f'Selected Config: |{option}|')

    options = config_options[option]
    options.append(Separator())
    options.append(Choice(value=None, name="Exit"))

    config = configparser.ConfigParser()
    config.read('config/config.ini')

    option_select = inquirer.select(
        message="Select an action:",
        choices=options,
        default=1,
    ).execute()

    info_logger.info(f'Selected Config 2: |{option_select}|')

    if option == "Sort Settings":
        if option_select == "Sort by Title":
            config.set('sorting', 'sort_title', 'True')
            config.set('sorting', 'sort_date', 'False')

        elif option_select == "Sort by Date":
            config.set('sorting', 'sort_date', 'True')
            config.set('sorting', 'sort_title', 'False')

    elif option == "Logging Settings":
        if option_select == "Log All":
            config.set('logging', 'log_all', 'True')
            config.set('logging', 'log_errors', 'False')
            config.set('logging', 'log_nothing', 'False')

        elif option_select == "Log Errors":
            config.set('logging', 'log_errors', 'True')
            config.set('logging', 'log_all', 'False')
            config.set('logging', 'log_nothing', 'False')
        
        elif option_select == "Log Nothing":
            config.set('logging', 'log_nothing', 'True')
            config.set('logging', 'log_all', 'False')
            config.set('logging', 'log_errors', 'False')
    elif option == "Steam Settings":
        if option_select == "Show URLs":
            config.set('steam', 'url', 'True')
            config.set('steam', 'no_url', 'False')
        elif option_select == "Dont Show URLs":
            config.set('steam', 'url', 'False')
            config.set('steam', 'no_url', 'True')
    
    else:
        error_logger.error(f'error at option_select, option picking.')


    with open('config/config.ini', 'w') as configfile:
        config.write(configfile)

    print("Exiting script to apply changes.")
    exit()