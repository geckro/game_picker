from sys import argv
def main():
        #TODO option menu should be moved into its own python file and be a lot smarter.
        option_menu = ("""OPTIONS
                       
╔ 1 
╠═══  RANDOMIZE
╠═══  LIST 

╔ 2 
╠═══  all
╠═══  system 
╠═══  date

╔ 3 
╠═══  system - console
╠═══  sort
╠═══  

╔ 4 
╠═══  system - console - sort
""")
        if argv[1].lower() == "--help" or argv[1].lower() == "help":
            print(option_menu)
            exit()
        if argv[2].lower() == "--help" or argv[2].lower() == "help":
            print(option_menu)
            exit()
            
        # TODO: Move these variables to var_storage.py
        opt1_list = ["randomize", "random", "list"]
        opt2_list = ["all", "everything", "console", "system", "date"]
        random = ["random", "randomize"]
        list = ["list"]
        all = ["all", "everything"]
        console = ["console", "system"]
        date = ["date"]
        sort = ["sort"]
        
        argv[1].lower()
        argv[2].lower()
        if argv[1] in opt1_list and argv[2] in opt2_list:
            if argv[1] in random:
                if argv[2] in all:
                    from lib.randomize import random_all
                    random_all()
                elif argv[2] in console:
                    from lib.randomize import random_sys
                    random_sys()
            elif argv[1] in list:
                if argv[2] in all:
                    print("Are you sure? Type 'Yes' to continue")
                    all_input = input("TYPE: ")
                    if all_input == "Yes":
                        pass
                    else:
                        exit()
                    from lib.list import list_all
                    list_all()
                elif argv[2] in console:
                    from lib.list import list_console
                    list_console()
                elif argv[2] in date:
                    if len(argv[3]) == 6:
                        pass
                    else:
                        print("ERROR! Did you enter a 6 character date?")
                        exit()
                    from lib.list import list_date
                    list_date()
                    
if __name__ == "__main__":
    main()