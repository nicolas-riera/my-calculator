# Libraries

import time

# Functions

def error():

    '''
    Function to print an error message when it happens.
    '''

    print("Choice not recognized.")
    time.sleep(0.2)
    input("Press Enter to try again.")

def calc_error():

    '''
    Function to print an error message for the calculator when it happens.
    '''

    print("An error has appeared. Please enter an operator first.")
    time.sleep(0.2)
    input("Press Enter to try again.")

def calc_divive_zero_error():

    '''
    Function to print an error message for the divisions when divided by zero.
    '''
    
    print("Illegal operation. Cannot divide by zero.")
    time.sleep(0.2)
    input("Press Enter to try again.")

def check_calc_syntax(calc_list):

    '''
    
    Function to check an error if there is two operators or two different numbers next to each other in the list.
    
    '''
    
    check_value_int = True
    for e in calc_list:
        if check_value_int:
            try:
                float(e)
                check_value_int = False
            except:
                print("Syntax error. Multiple operators next to each other detected.")
                time.sleep(0.2)
                input("Press Enter to try again.")
                return False
        else:
            if e in ["+", "*", "x", ":", "/", "-"]:
                check_value_int = True
            else:
                print("Syntax error. Multiple numbers next to each other detected.")
                time.sleep(0.2)
                input("Press Enter to try again.")
                return False
    return True