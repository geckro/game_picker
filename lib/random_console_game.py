def def_random_console_game():
    # Logging
    from setting import log 
    log()
    from logging import debug

    
    from lib.var_storage import consoleList,consoleListVar
    from random import randrange
    whileStop = 0
    while whileStop != 1:
        print("Options are:",consoleListVar)
        consoleInput = input("TYPE: ")
        print(consoleList)
        if consoleInput in consoleList:
            whileStop = 1
            break
        print("Did you mistype something?")
    whileStop = 0
    from random_line import lines
    
    whileStop = 0
    from csv import reader
    while whileStop != 1:
        with open("./sources/games.csv", "r") as temp2:

            # Prints a random number from the number set in the variable lines
            randomLine = randrange(lines)
            print("INFO: Random Line:",randomLine + 1)

        temp2.close()

        # Interacting with ./sources/games.csv

        with open("./sources/games.csv", "r") as games_csv:
            read_csv = reader(games_csv)
            for i in range(randomLine):
                next(read_csv)
            row = next(read_csv)
            
            debug("row: " + str(row)) # DEBUG logging

            # from the selected row, make console variable
            consoleRow = (row[1])

            debug("line & randomLine: " + str(lines), str(randomLine)) # DEBUG logging
            
            # if the console variable matches the random console selected, exit while loop
            if "["+consoleInput+"]" in consoleRow:
                whileStop = 1
                n = row[0]
                break
    print("Your game is:",n.strip("[]"))