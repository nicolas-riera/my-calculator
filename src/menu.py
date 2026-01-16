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
                    print(f"{Fore.red}1. Calculate")
                    print(f"{Fore.blue}2. History")
                    print(f"{Fore.black}0. Exit")
                    usr_input = int(input(f"{Fore.white}Enter your choice...\n"))
                else:
                    print(f"{Fore.red}1. Calculate")
                    print(f"{Fore.blue}2. History")
                    print(f"{Fore.yellow}3. Erase result")
                    print(f"{Fore.black}0. Exit{Style.reset}")
                    usr_input = int(input(f"Enter your choice...\n"))
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
