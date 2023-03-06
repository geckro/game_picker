from os.path import basename
u8 = "UTF8"

# The file path of the csv file
csv = "src/games.csv"

# name of current file, useful for error handling
filename = basename(__file__)

# options for main
RANDOMIZE = "Randomize"
LIST = "List"
CONFIG = "Config"
OTHER = "Misc"
EXIT = "Exit"
resultfile = "resultfile.txt"

# This is a dictionary that maps each action to its corresponding options
options = {
    RANDOMIZE: [
        "Randomize Everything",
        "Randomize Console",
        "Randomize Date",
        "Randomize Developer",
    ],
    LIST: [
        "List Everything",
        "List Console",
        "List Date",
        "List Developer",
        "List Games on Steam",
    ],
    OTHER: [
        "Search Games",
        "Owned Games",
    ]
}

