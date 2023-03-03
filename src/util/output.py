# Prints the output.
bold = "\033[1m"
red = "\033[0;31m"
green = "\033[0;32m"
yellow = "\033[0;33m"
blue = "\033[0;34m"
purple = "\033[0;35m"
cyan = "\033[0;36m"
white = "\033[0;37m"
reset = "\033[0m"
orange = "\x1b[38;2;255;165;0m"

import configparser

def print_output(csv_column, date, config):
    config_map = {
        "no_title": False,
        "no_system": False,
        "no_date": False,
        "no_series": False,
        "no_version": False,
        "no_region": False,
        "no_sequel": False,
        "no_developer": False,
        "no_publisher": False,
        "no_genre": False,
        "no_alt_names": False,
        "no_steam_id": False,
        "null": False,
    }
    config_map[config] = True

    config = configparser.ConfigParser()
    config.read('config/config.ini')
    steam_urls = config.getboolean('steam', 'url')
    no_steam_urls = config.getboolean('steam', 'no_url')

    csv_title = "" if config_map['no_title'] else f"{bold}{csv_column[0]}{reset}"
    csv_system = "" if config_map['no_system'] else f"{red}{csv_column[1]}{reset}"
    csv_date = "" if config_map['no_date'] else f"{green}{date}{reset}"
    csv_series = "" if config_map['no_series'] else f"{green}{csv_column[3]}{reset}"
    csv_version = "" if config_map['no_version'] else f"{green}{csv_column[4]}{reset}"
    csv_region = "" if config_map['no_region'] else f"{green}{csv_column[5]}{reset}"
    csv_sequel = "" if config_map['no_sequel'] else f"{green}{csv_column[6]}{reset}"
    csv_developer = "" if config_map['no_developer'] else f"{green}{csv_column[7]}{reset}"
    csv_publisher = "" if config_map['no_publisher'] else f"{green}{csv_column[8]}{reset}"
    csv_genre = "" if config_map['no_genre'] else f"{green}{csv_column[9]}{reset}"
    csv_alt_names = "" if config_map['no_alt_names'] else f"{green}{csv_column[10]}{reset}"
    if steam_urls == True:
        csv_steam = "" if config_map['no_steam_id'] else f"{purple}https://store.steampowered.com/app/{csv_column[11]}{reset}"
    elif no_steam_urls == True:
        csv_steam = "" if config_map['no_steam_id'] else f"{purple}{csv_column[11]}{reset}"

    csv_components = [
        csv_title,
        csv_system if not config_map['no_system'] else "",
        csv_date if not config_map['no_date'] else "",
        csv_series if not config_map['no_series'] else "",
        csv_version if not config_map['no_version'] else "",
        csv_region if not config_map['no_region'] else "",
        csv_sequel if not config_map['no_sequel'] else "",
        csv_developer if not config_map['no_developer'] else "",
        csv_publisher if not config_map['no_publisher'] else "",
        csv_genre if not config_map['no_genre'] else "",
        csv_alt_names if not config_map['no_alt_names'] else "",
        csv_steam if not config_map['no_steam_id'] else "",
    ]

    return ", ".join([component for component in csv_components if component])