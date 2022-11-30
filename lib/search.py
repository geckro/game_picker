def search_games():
    # Logging
    from lib.setting import log 
    log()
    from logging import debug

    # If this variable is not declared in def() then while loop will not function correctly
    whileStop = 0

    while whileStop != 1:
        game_input = input("Search term: ")
        # if the search term isn't blank then try searching
        if game_input != "":
            whileStop = 1
            debug("game_input_success: " + str(game_input)) # Logging
            break
        # if the search term is blank then print this
        print("Did you even type something?")
        debug("game_input_failure: " + str(game_input)) # Logging

    from csv import reader
    with open("./sources/games.csv", "r") as games_csv:
        read_csv = reader(games_csv)
        for row in read_csv:

            # This might be done as a mistake and searching a big .csv file could get annoying
            if len(game_input) == 1:
                from lib.var_storage import yes
                temp_input = input("Are you sure you really want to search this?")
                if temp_input in yes:
                    if game_input in row[0]: 
                        print(row[0])
                else:
                    return

            # IF the game input is in all lowercase or uppercase, search the file in lc/uc.
            elif game_input.islower() or game_input.isupper():
                if game_input in row[0].lower():  
                    print(row[0])
                elif game_input in row[0].upper():  
                    print(row[0])

            # IF the game input isnt all lowercase, try searching anyway
            elif game_input in row[0]:  
                print(row[0])