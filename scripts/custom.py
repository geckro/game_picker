def defcustom():
    from variable_storage import custom_input_options,custom_input_options_var
    x = 0
    while x != 1:
        print(custom_input_options_var)
        custom_input = input("TYPE: ")
        if custom_input in custom_input_options:
            x = 1
            break
        print("Did you mistype something?")
    if custom_input == 'add':
        print("NOTE: This tool is limited in single variables. If you want to add multiple, do it manually. the csv file is located at ./sources/custom.csv")
        name = input("Game title: ")
        console = input("Console: ")
        date = input("Date: ")
        score = input("Score: ")
        genre = input("Genre: ")
        developer = input("Developer:" )
        publisher = input("Publisher: ")
        #TODO
        # Finish add custom_input
        
    #TODO
    #Delete custom_input

    #TODO
    #List all custom inputs