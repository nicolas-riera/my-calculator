import time
from src.calculator import calculator
def menu(result):
    if result == "":
        while True:
            try:
                usr_input = int(input("1. Calculate\n2. History\n0. Exit\\nEnter your choice...\n"))
            except ValueError:
                print("Choice not recognized. Please try again")
                continue

            match usr_input:
                case 1:
                    calculator()
                case 2:
                    pass
                case 0:
                    exit()
                case _:
                    print("Error. Please try again.")
                    time.sleep(0.2)
                    continue

    else: 
        while True:
            try:
                usr_input = int(input("1. Calculate\n2. History\n3. Erase result\n0. Exit\\nEnter your choice..."))
            except ValueError:
                print("Choice not recognized. Please try again")
                continue

            match usr_input:
                case 1:
                    pass
                case 2:
                    pass
                case 3:
                    pass
                case 0:
                    exit()
                case _:
                    print("Error. Please try again.")
                    time.sleep(0.2)
                    continue