import logging

from InquirerPy import inquirer
from InquirerPy.base import Choice
from InquirerPy.separator import Separator
from src.randomize_games import randomize_games
from src.list_games import list_games

def main() -> None:
    
    logging.basicConfig(level=logging.INFO)

    # Asks the user for an action and then saves it in selected_options_1
    selected_options_1 = inquirer.select(
        message="Select an action:",
        choices=[
            "Randomize",
            "List",
            Separator(),
            Choice(value=None, name="Exit"),
        ],
        default=1,
    ).execute()

    # Log the selected option for the first select inquiry.
    logging.info(f'Selected Options 1: |{selected_options_1}|')

    if selected_options_1:

        # This is a dictionary that maps each action to its corresponding options
        options = {
            "Randomize": [
                "Randomize Everything",
                "Randomize Console",
            ],
            "List": [
                "List Everything",
                "List Console",
                "List Date",
                "List Developer",
            ],
        }

        # Append separator and exit to the list of options for the selected action
        options[selected_options_1].append(Separator())
        options[selected_options_1].append(Choice(value=None, name="Exit"))

        # Display the second prompt to the user using the options for the selected action
        selected_options_2 = inquirer.select(
            message="Select an action:",
            choices=options[selected_options_1],
            default=1,
        ).execute()

        # Log the selected option for the first and second select inquiry.
        logging.info(f'Selected Options 1 (Again): |{selected_options_1}|')
        logging.info(f'Selected Options 2: |{selected_options_2}|')

        # Define a dictionary that maps each action to its corresponding function
        actions = {
            "Randomize Everything": randomize_games,
            "Randomize Console": randomize_games,
            "List Everything": list_games,
            "List Console": list_games,
            "List Date": list_games,
            "List Developer": list_games,
        }

        if selected_options_2:
            # Get the function that corresponds to the selected action
            execute_code = actions.get(selected_options_2)
            if execute_code:
                
                # Log execute_code
                logging.info(f'What code are you executing?: |{execute_code}|')
                
                # Call the function
                execute_code(selected_options_2)

if __name__ == "__main__":
    main()