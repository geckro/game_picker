def def_random():
    from lib.random_line import lines
    print("Done")

    from lib.setting import log 
    log()
    from logging import debug

    class rcg:
        from random import choice
        from lib.var_storage import consoleListSingular
        tempConsole = []
        for i in range(3):
            random_choice = choice(consoleListSingular)
            tempConsole.append(random_choice)
            debug("tempConsole: ",tempConsole) # Logging
        randConsole = choice(tempConsole)
        debug("randConsole: ",randConsole) # Logging

        print(randConsole)

    class console_num:
        if rcg.randConsole == "nes":
            consoleNum = "01"
        elif rcg.randConsole == "sfc":
            consoleNum = "02"
        elif rcg.randConsole == "n64":
            consoleNum = "03"
        elif rcg.randConsole == "gcn":
            consoleNum = "04"
        elif rcg.randConsole == "wii":
            consoleNum = "05"
        elif rcg.randConsole == "vby":
            consoleNum = "06"
        elif rcg.randConsole == "nds":
            consoleNum = "07"

        print(consoleNum)

    class pick_game:
        from csv import reader
        whileStop = 0
        while whileStop != 1:

            with open("./sources/games.csv", "r") as temp2:
                # Prints a random number from the number set in the variable lines
                from random import randrange
                randomLine = randrange(lines)
            temp2.close()

            with open("./sources/games.csv", "r") as games_csv:
                read_csv = reader(games_csv)
                for i in range(randomLine):
                    next(read_csv)
                row = next(read_csv)

                # from the selected row, make console variable
                consoleRow = (row[1])
                # if the console variable matches the random console selected, exit while loop
                if console_num.consoleNum in consoleRow:
                    whileStop = 1
                    game = row[0]
                    if row[2] != "":
                        date = row[2]
                    else:
                        date = "NO DATE"
                    break
        print("Game Title     :       ",game)
        print("Console        :       ",rcg.randConsole)
        print("Date           :       ",date)
