try:
    import os
    from InquirerPy import inquirer
    from InquirerPy.base import Choice
    from InquirerPy.separator import Separator
    from src.randomize_games import randomize_games
    from src.list_games import list_games
    from src.owned_games import owned_games
    from src.search import search_csv
    from src.config import configure_settings
    from src.logging_config import *
    from src.util.variables import *
except ModuleNotFoundError as ERR:
    error_logger.error(f"Failed to import {ERR.name} module: {ERR}")

def main() -> None:

    info_logger.info(f'Starting Program...')

    if os.path.exists(resultfile):
        os.remove(resultfile)
        info_logger.info(f"File {resultfile} has been deleted.")
    else:
        info_logger.info(f"File {resultfile} does not exist.")

    # Asks the user for an action and then saves it in selected_options_1
    selected_options_1 = inquirer.select(
        message="Select an action:",
        choices=[
            RANDOMIZE,
            LIST,
            OTHER,
            Separator(), 
            CONFIG,
            Choice(value=None, name=EXIT),
        ],
        default=1,
    ).execute()

    # Log the selected option for the first select inquiry.
    info_logger.info(f'Selected Options 1: |{selected_options_1}|')

    if selected_options_1:
        if CONFIG in selected_options_1:
            configure_settings()
        else:
            # Append separator and exit to the list of options for the selected action
            options[selected_options_1].append(Separator())
            options[selected_options_1].append(Choice(value=None, name=EXIT))

            # Display the second prompt to the user using the options for the selected action
            selected_options_2 = inquirer.select(
                message="Select an action:",
                choices=options[selected_options_1],
                default=1,
            ).execute()

            # Log the selected option for the first and second select inquiry.
            info_logger.info(f'Selected Options 1 (Again): |{selected_options_1}|')
            info_logger.info(f'Selected Options 2: |{selected_options_2}|')

            # Define a dictionary that maps each action to its corresponding function
            actions = {
                "Randomize Everything": randomize_games,
                "Randomize Console": randomize_games,
                "Randomize Date": randomize_games,
                "Randomize Developer": randomize_games,
                "List Everything": list_games,
                "List Console": list_games,
                "List Date": list_games,
                "List Developer": list_games,
                "List Games on Steam": list_games,
                "Search Games": search_csv,
                "Owned Games": owned_games,
            }

            if selected_options_2:
                # Get the function that corresponds to the selected action
                execute_code = actions.get(selected_options_2)
                if execute_code:
                    
                    # Log execute_code
                    info_logger.info(f'What code are you executing?: |{execute_code}|')
                    
                    # Call the function
                    if selected_options_2 != "Search Games" and selected_options_2 != "Owned Games":
                        execute_code(selected_options_2)
                    else:
                        execute_code() 

    info_logger.info(f'Exiting main...')

if __name__ == "__main__":
    main()