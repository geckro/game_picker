if __name__ == "__main__":
    # Logging
    from lib.setting import log 
    log()
    from logging import info,debug
    x = range(6)
    for n in x:
        print(n)
    
    whileStop = 0
    while whileStop != 1:
        from lib.var_storage import accepted_decisions

        from lib.var_storage import accepted_decisions_var
        print(accepted_decisions_var)

        dec = input("What do you want to do: ")
        if dec in accepted_decisions:
            whileStop = 1
            break
        print("Did you mistype something?")

        info("user_decision: " + dec) 
        debug("whileStop: " + str(whileStop)) 

    if dec == 'random':
        from lib.random_game import def_random
        def_random()
    elif dec == 'list_console_games' or dec == 'lcg':
        from lib.list_console_games import def_list_console_games as lcg
        lcg()
    elif dec == 'random_console_games' or dec == 'rcg':
        from lib.random_console_game import def_random_console_game as rcg
        rcg()
    elif dec == 'clearlog':
        from lib.clearlog import clear_log
        clear_log()
    elif dec == 'search':
        from lib.search import search_games
        search_games()
    elif dec == 'custom':
        from lib.custom import defcustom
        defcustom()