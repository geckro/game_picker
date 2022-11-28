def def_list_console_games():
    from variable_storage import consoleList
    whileStop = 0
    while whileStop != 1:
        print("Options are:",consoleList)
        consoleInput = input("Which Console: ")
        if consoleInput in consoleList:
            whileStop = 1
            break
        print("Did you mistype something?")
    whileStop = 0
    from csv import reader
    with open("./sources/games.csv", "r") as games_csv:
        read_csv = reader(games_csv, delimiter=';')
        print("List of",consoleInput.capitalize(),"games")
        for row in read_csv:
            if "["+consoleInput+"]" in row[1]:
                print(row[2].strip('[]'),"|",row[0].strip('[]'))