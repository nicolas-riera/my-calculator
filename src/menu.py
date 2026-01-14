# Libraries

from src.calculator import *
from src.clear import clear
from src.error import error

# Functions

def menu():

    result = None
    calc_input = None

    while True:
        if result == None:
            try:
                usr_input = int(input("1. Calculate\n2. History\n0. Exit\nEnter your choice...\n"))
                clear()
            except ValueError:
                error()
                clear()
                continue

            match usr_input:
                case 1:
                    result = calc_result(calc_input, result)
                case 2:
                    pass
                case 0:
                    clear()
                    exit()
                case _:
                    error()
                    continue

        else: 
            try:
                usr_input = int(input("1. Calculate\n2. History\n3. Erase result\n0. Exit\nEnter your choice...\n"))
                clear()
            except ValueError:
                error()
                clear()
                continue

            match usr_input:
                case 1:
                    result = calc_result(calc_input, result)
                case 2:
                    pass
                case 3:
                    result = erase_result(result)
                case 0:
                    exit()
                case _:
                    error()
                    continue
