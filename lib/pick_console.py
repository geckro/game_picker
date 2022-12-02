def random_console():
    from random import choice
    from lib.var_storage import consoleListSingular
    tempConsole = []
    for i in range(3):
        random_choice = choice(consoleListSingular)
        tempConsole.append(random_choice)
    randConsole = choice(tempConsole)

    print(randConsole)