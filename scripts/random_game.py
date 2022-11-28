def def_random():
    from random import choice,randrange
    from csv import reader
    from time import sleep
    from variable_storage import consoleList
    tempConsole = []
    rand1 = choice(consoleList)
    tempConsole.append(rand1)
    rand2 = choice(consoleList)
    tempConsole.append(rand2)
    rand3 = choice(consoleList)
    tempConsole.append(rand3)
    randConsole = choice(tempConsole)

    print("INFO: tempRand:",rand1,rand2,rand3)
    print("INFO: randConsole:",randConsole)
    sleep(2.5)

    from random_line import lines
    
    whileStop = 0
    while whileStop != 1:

        with open("./sources/games.csv", "r") as temp2:

            # Prints a random number from the number set in the variable lines
            randomLine = randrange(lines)
            print("INFO: Random Line:",randomLine + 1)

        temp2.close()

        # Interacting with ./sources/games.csv

        with open("./sources/games.csv", "r") as games_csv:
            read_csv = reader(games_csv, delimiter=';')
            for i in range(randomLine):
                next(read_csv)
            row = next(read_csv)
            print(row)

            # from the selected row, make console variable
            consoleRow = (row[1])
            print(lines, randomLine, randConsole)
            # if the console variable matches the random console selected, exit while loop
            if "["+randConsole+"]" in consoleRow:
                whileStop = 1
                n = row[0]
                break
    print("Your game is:",n)