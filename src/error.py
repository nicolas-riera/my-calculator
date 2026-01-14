import time

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
    Function to print an error message for the calculator when it happens.
    '''
    
    print("Illegal operation. Cannot divide by zero.")
    time.sleep(0.2)
    input("Press Enter to try again.")
