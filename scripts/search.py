def search_games():
    whileStop = 0
    while whileStop != 1:
        gameInput = input("Which Game: ")
        if gameInput != "":
            whileStop = 1
            break
        print("Did you mistype something?")
    whileStop = 0
    from csv import reader
    with open("./sources/games.csv", "r") as games_csv:
        read_csv = reader(games_csv, delimiter=';')
        for row in read_csv:
            if gameInput.islower():
                    if gameInput in row[0].lower():  
                        print(row[0].strip('[]'))
            elif gameInput in row[0]:  
                print(row[0].strip('[]'))