def def_list_console_games():
    from lib.var_storage import consoleList,consoleListSingular
    whileStop = 0
    while whileStop != 1:
        print("Options are:",consoleListSingular)
        consoleInput = input("Which Console: ")
        if consoleInput in consoleList:
            whileStop = 1
            break
        print("Did you mistype something?")
    whileStop = 0
    class console_num:
        from lib.var_storage import console_nes,console_sfc,console_n64,console_gcn,console_wii,console_vby,console_nds
        if consoleInput in console_nes:
            consoleNum = "01"
        elif consoleInput in console_sfc:
            consoleNum = "02"
        elif consoleInput in console_n64:
            consoleNum = "03"
        elif consoleInput in console_gcn:
            consoleNum = "04"
        elif consoleInput in console_wii:
            consoleNum = "05"
        elif consoleInput in console_vby:
            consoleNum = "06"
        elif consoleInput in console_nds:
            consoleNum = "07"
    
    from csv import reader
    with open("./sources/games.csv", "r") as games_csv:
        read_csv = reader(games_csv)
        print("List of",consoleInput.capitalize(),"games")
        for column in read_csv:
            if console_num.consoleNum in column[1]:
                print(column[2],"|",column[0])