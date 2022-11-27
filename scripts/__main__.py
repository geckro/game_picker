if __name__ == "__main__":
    
    # Logging
    from setting import log 
    log()
    from logging import info,debug
    
    x = 0
    while x != 1:
        from variable_storage import accepted_decisions

        from variable_storage import accepted_decisions_var
        print(accepted_decisions_var)

        dec = input("What do you want to do: ")
        if dec in accepted_decisions:
            x = 1
            break
        print("Did you mistype something?")

        info("user_decision: " + dec) 
        debug("x: " + str(x))

    if dec == 'random':
        from random_game import def_random
        def_random()
    elif dec == 'list_console_games' or dec == 'lcg':
        from list_console_games import def_list_console_games
        def_list_console_games()
    elif dec == 'random_console_games' or dec == 'rcg':
        from random_console_game import def_rand_console_games
        def_rand_console_games()
    elif dec == 'clearlog':
        from clearlog import c_log
        c_log()
    elif dec == 'search':
        from search import search_games
        search_games()