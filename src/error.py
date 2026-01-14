import time
def error():
    '''Function to print an error message when it happens.
    '''
    print("Choice not recognized.")
    time.sleep(0.2)
    input("Press enter to try again.")

def calc_error():
    '''Function to print an error message for the calculator when it happens.
    '''
    print("An error has appeared. Please enter an operator first.")
    time.sleep(0.2)
    input("Press enter to try again.")
