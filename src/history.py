# Librairies

import json

from src.clear import clear
from src.error import *

# Functions

def create_json_if_not_found():
    try :
        with open("history.json", "r") as f:
            history = json.load(f)
    except:
        clear_history()

def write_history(calc_input, result):

    '''
    Function to write history into a dictionnary list to convert it in a json.
    
    PARAMETERS -
    calc_input : The function take the input entered by the user for the calculation.
    result : The function take the result of the calculation entered by the user.
    '''

    entry = {"input": calc_input, "result": result}

    with open("history.json", "r") as f:
        history = json.load(f)

    history.append(entry)

    with open("history.json", "w") as f:
        json.dump(history, f, indent=4)

def clear_history():

    '''
    Function to clear the history when the user enter the correct input.
    '''

    with open('history.json', 'w') as f:
        json.dump([], f)

def display_history():

    '''
    Function to display the history correctly into the menu.

    RETURN -
    display_input(): Function return itself if there's an error.
    '''
    
    with open("history.json", "r") as f:
        history = json.load(f)

    clear()

    # Check if history is empty
    if history == []:
        print("There's no history yet. Please try to calculate first.")
        time.sleep(0.2)
        input("Press Enter to continue")

    else:
        
        print("History :\n")

        for e in history:
            print(f"{Fore.cyan}{e["input"]} {Fore.white}= {Fore.blue}{e["result"]}\n")

        try:
            usr_input = int(input(f"{Fore.red}1. Clear History\n{Fore.black}0. Exit\n{Fore.white}Enter your choice...\n"))
     
        except ValueError:
            clear()
            error()
            clear()
            display_history()

        match usr_input:

            case 1:
                clear_history()
                clear()
                print("History has been cleared !")
                time.sleep(0.2)
                input("Press Enter to continue")

            case 0:
                pass

            case _:
                clear()
                error()
                clear()
                return display_history()
                   
    clear()
   