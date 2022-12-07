def list_all():
    print("list_all")
    from csv import reader
    with open("./sources/games.csv", "r", encoding="UTF8") as games_csv:
        read_csv = reader(games_csv)
        print("List of","games")
        for column in read_csv:
                print(column[2],"|",column[0])
def list_console():
    class console_num:
        from lib.var_storage import console_nes,console_sfc,console_n64,console_gcn,console_wii,console_vby,console_nds
        from sys import argv
        try:
            if str(argv[3]).lower() == "date" and str(argv[4]).lower() != "date":
                date_var = 0
            elif argv[3].lower() == "date" or argv[4].lower() == "date":
                date_var = 1    
        except IndexError:
            date_var = 0
            pass 
        if argv[3] in console_nes:
                consoleNum = "01"
                consoleName = "Nintendo Entertainment System"
        elif argv[3] in console_sfc:
            consoleNum = "02"
            consoleName = "Super Nintendo"
        elif argv[3] in console_n64:
            consoleNum = "03"
            consoleName = "Nintendo 64"
        elif argv[3] in console_gcn:
            consoleNum = "04"
            consoleName = "GameCube"
        elif argv[3] in console_wii:
            consoleNum = "05"
            consoleName = "Wii"
        elif argv[3] in console_vby:
            consoleNum = "06"
            consoleName = "Virtual Boy"
        elif argv[3] in console_nds:
            consoleNum = "07"
            consoleName = "Nintendo DS"
    from csv import reader
    with open("./sources/games.csv", "r", encoding="UTF8") as games_csv:
        read_csv = reader(games_csv)
        print("List of",console_num.consoleName,"games")
        print("DATE      |      NAME      |      SERIES")
        
        # TODO: Make function print multiple lines
        # If sort date is wanted, write the results to a file, sort it alphabetically, and then print results.
        if console_num.date_var == 1:
            temp = open('temp.txt', 'w')
            temp.close()    
            for column in read_csv:
                if console_num.consoleNum in column[1]:
                    temp = open('temp.txt', 'a')
                    temporary = column[2],column[0]
                    temp.write(str(temporary) + "\n")
                    temp.close()
            with open("temp.txt", "r+") as file:
                    temp2 = sorted(file.readlines())
                    
                    file.write(str(temp2))
        
        #  If sort date is not wanted, just list from the csv file.
        for column in read_csv:
                if console_num.consoleNum in column[1]:
                    print(column[2],"|",column[0],"|",column[3])
def list_date():
    print("list_date")
    from sys import argv
    from csv import reader
    with open("./sources/games.csv", "r", encoding="UTF8") as games_csv:
        read_csv = reader(games_csv)
        for column in read_csv:
            if argv[3] in column[2]:
                print(column[1],"|",column[0])