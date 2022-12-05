from sys import argv
def main():
        if argv[1].lower() == "--help" or argv[1].lower() == "help":
            print("Options:")
            print("randomize")
            exit()
        if argv[2].lower() == "--help" or argv[2].lower() == "help":
            print("Options:")
            print("all")
            exit()    
        opt1_list = ["randomize", "random"]
        opt2_list = ["all", "everything", "console", "system"]
        random = ["random", "randomize"]
        all = ["all", "everything"]
        console = ["console", "system"]
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
if __name__ == "__main__":
    main()