# Libraries

from src.calculator import *
from src.clear import clear
from src.error import error
from src.history import *
from colored import Fore

# Functions

def menu():

    '''
    Function that print the menu in the terminal, and call other functions to do the logic.
    '''

    result = None
    calc_input = None

    while True:
        
            try:
                # Different menus depending on the state of the calculator
                if result == None:
                    usr_input = int(input(f"{Fore.red}1. Calculate\n{Fore.blue}2. History\n{Fore.black}0. Exit\n{Fore.white}Enter your choice...\n"))
                else:
                    usr_input = int(input(f"{Fore.red}1. Calculate\n{Fore.blue}2. History\n{Fore.yellow}3. Erase result\n{Fore.black}0. Exit\n{Fore.white}Enter your choice...\n"))
                clear()

            except ValueError:
                clear()
                error()
                clear()
                continue

            match usr_input:

                case 1:
                    result = calc_result(calc_input, result)

                case 2:
                    display_history()
                    
                case 3:
                    if result != None:
                        result = erase_result(result)
                    else:
                        error()
                        clear()

                case 0:
                    clear()
                    exit()

                case _:
                    error()
                    clear()
