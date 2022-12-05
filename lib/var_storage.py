consoleList = [
    "nintendo entertainment system", "nes", "famicom",
    "super nintendo entertainment system", "snes", "super famicom","super nintendo",
    "nintendo 64", "n64",
    "gamecube", "gcn", "ngc",
    "wii",
    "virtual boy", "vby", "vb"
    "nintendo ds", "ds", "nds",

]
console_nes = ["nintendo entertainment system", "nes", "famicom"]
console_sfc = ["super nintendo entertainment system", "snes", "super famicom","super nintendo"]
console_n64 = ["nintendo 64", "n64"]
console_gcn = ["gamecube", "gcn", "ngc"]
console_wii = ["wii"]
console_vby = ["virtual boy", "vby", "vb"]
console_nds = ["nintendo ds", "ds", "nds"]

consoleListSingular = ["nes","sfc","n64","gcn","wii","vby","nds"]
consoleListVar = """-= CONSOLE LIST =-
NES, SNES, N64, GCN, WII"""
accepted_decisions = ['random', 'list_console_games', 'lcg', 'random_console_game', 'rcg', 'clearlog', 'search', 'custom']
accepted_decisions_var = """\n ✅ ACCEPTED DECISIONS ✅ \n
 ❓ random              =   picks a random game from a random console.
 🎚️  list_console_games  =   lists all games in database for inputted console.
 ❓ random_console_game =   picks a random game for inputted console.
 🎗️  clearlog            =   clears <log.log>.
 custom_input            =  allows you to input custom games
 search                  = searches the file for a game.
"""
custom_input_options = ['add', 'remove', 'list']
custom_input_options_var = """\n CUSTOM INPUT OPTIONS \n
add              =   add game to custom.csv
remove           =   remove game to custom.csv
list             =   list entries in custom.csv
"""
yes = ['yes', 'y', 'yeah', 'ye', 'yea']
no = ['no', 'n', 'nah']
console_dictionary = {
        "nes":"01",
        "sfc":"02",
        "n64":"03",
        "gcn":"04",
        "wii":"05",
        "vby":"06",
        "nds":"07",
        "gba":"08",
        "gby":"09",
        "gbc":"10",
        "3ds":"11",
        "ps1":"12",
        "ps2":"13",
        "ps3":"14",
        "ps4":"15",
        "ps5":"16",
        "swi":"17",
        "wiu":"18",
        "psp":"19",
        "psv":"20"
    }

