
# class random_line:
#     with open("./sources/games.csv", "r", encoding="utf8") as temp:
#     # Count amount of lines in the file
#         for filesize, line in enumerate(temp):
#                 pass
#     lines = filesize + 1
#     #print("INFO: Lines:",lines)
#     temp.close()
# class random_console:
#     from sys import argv
#     all = ["all", "everything"]
#     if argv[2] in all:
#         from random import choice
#         from lib.var_storage import consoleListSingular
#         tempConsole = []
#         for i in range(3):
#             random_choice = choice(consoleListSingular)
#             tempConsole.append(random_choice)
#         console = choice(tempConsole)
#     else:
#         console = argv[3].lower()
        
# class console_num:
#     from lib.var_storage import console_dictionary
#     console_num = console_dictionary[random_console.console]
# from lib.setting import log 
# log()
# from logging import debug
# def random_all():
#     class random_all:
#         from csv import reader
#         whileStop = 0
#         while whileStop != 1:

#             with open("./sources/games.csv", "r", encoding="UTF8") as temp2:
#                 # Prints a random number from the number set in the variable lines
#                 from random import randrange
#                 randomLine = randrange(random_line.lines)
#             temp2.close()

#             with open("./sources/games.csv", "r", encoding="UTF8") as games_csv:
#                 read_csv = reader(games_csv)
#                 for i in range(randomLine):
#                     next(read_csv)
#                 row = next(read_csv)

#                 # from the selected row, make console variable
#                 consoleRow = (row[1])
#                 # if the console variable matches the random console selected, exit while loop
#                 if console_num.console_num in consoleRow:
#                     whileStop = 1
#                     game = row[0]
#                     if row[2] != "":
#                         date = row[2]
#                     else:
#                         date = "NO DATE"
#                     if row[3] != "":
#                         series = row[3]
#                     else:
#                         series = "NULL"   
#                     break
#         print("Game Title     :       ",game)
#         print("Console        :       ",random_console.console)
#         print("Date           :       ",date)
#         print("Series         :       ",series)
# def random_sys():
#     class random_sys:
#         # Logging
#         from lib.setting import log
#         from csv import reader
#         from random import randrange
#         log()
#         whileStop = 0
#         while whileStop != 1:
#             with open("./sources/games.csv", "r", encoding="utf8") as temp2:
#                 # Prints a random number from the number set in the variable lines
#                 randomLine = randrange(random_line.lines)
#             temp2.close()

#             # Interacting with ./sources/games.csv

#             with open("./sources/games.csv", "r", encoding="utf8") as games_csv:
#                 read_csv = reader(games_csv)
#                 for i in range(randomLine):
#                     next(read_csv)
#                 row = next(read_csv)
#                 # from the selected row, make console variable
#                 consoleRow = (row[1])
                
#                 # if the console variable matches the random console selected, exit while loop
#                 if console_num.console_num in consoleRow:
#                     whileStop = 1
#                     n = row[0]
#                     break
#         if row[2] != "":
#             date1 = str(row[2])[:-2]
#             date2 = str(row[2])[-2:]
#             date = date1+"-"+date2
#         else:
#             date = "NULL"
#         if row[3] != "":
#             series = row[3]
#         else:
#             series = "NULL"    
#         print("Game Title     :       ",n)
#         print("Series         :       ",series)
#         print("Date           :       ",date)
def randomize_games():
    print("test")