def randConsole():
    from random import choice
    from lib.var_storage import consoleListSingular
    tempConsole = []
    for i in range(3):
        random_choice = choice(consoleListSingular)
        tempConsole.append(random_choice)
    randConsole = choice(tempConsole)
    return randConsole
def def_console_number(console):
    console_dictionary = {
        "nes":"01",
        "sfc":"02",
        "n64":"03",
        "gcn":"04",
        "wii":"05",
        "vby":"06",
        "nds":"07",
        "gba":"08",
        "gby":"09",
        "gbc":"10",
        "3ds":"11",
        "ps1":"12",
        "ps2":"13",
        "ps3":"14",
        "ps4":"15",
        "ps5":"16",
        "swi":"17",
        "wiu":"18",
        "psp":"19",
        "psv":"20"
    }
    import lib.random_game
    print(lib.random_game)
    console_num = console_dictionary[lib.random_game.randConsole]
    return console_num