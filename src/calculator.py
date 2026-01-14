# Libraries
import time
import re

from src.operations import *
from src.clear import clear
from src.error import *

# Functions

def calculator(result):
    '''The computer split the user input in a list to be calculated
    
    PARAMETERS -
    result : Function take the result to know if there is one or not
    
    RETURNS -
    calc_input: return the calcul entered by the user for the result display in the menu
    result: return the result of the calcul.'''

    if result == None:
        print("Current operators taken into accounts : ")
        print("+  |  -")
        print("*  or  x")
        print("/  or  :")
        calc_input = input("Write your calcul here...\n")
        if calc_input == "":
            calc_error()
            clear()
            calculator(result)
        elif calc_input[0].isdigit() == False:
            error()
            clear()
            calculator(result)
        
        else:
            calc_split = re.findall('[+-/*//()]+|\d+',calc_input)
            result = operation_prio_calc(calc_split)
            clear()
            return calc_input, result

    else:
        calc_input = input(f"Current calcul : {result} ...\n")
        if calc_input[0] not in ["+", "*", "x", ":", "/", "-"] or calc_input == "":
            calc_error()
            clear()
            calculator(result)
        elif calc_input[0].isdigit() == False:
            error()
            clear()
            calculator(result)
        else:
            calc_split = re.findall('[+-/*//()]+|\d+',calc_input)
            calc_split.insert(0, str(result))
            result = operation_prio_calc(calc_split)
            clear()
            return calc_input, result

def operation_prio_calc(calc_split:list):
    '''Function to manage the operations prio
    
    PARAMETERS -
    calc_split : the list that contain all the numbers and the operators
    
    RETURNS -
    result: return the result of the calcul.'''
    
    i = 0
    while i < len(calc_split):
        if calc_split[i] in ["x", "*", ":", "/"]:
            num1 = float(calc_split[i-1])
            num2 = float(calc_split[i+1])
            
            if calc_split[i] in ["x", "*"]:
                op_result = Operations.multiply(num1, num2)
            else:
                op_result = Operations.divide(num1, num2)
            
            calc_split[i-1 : i+2] = [str(op_result)]
            i -= 1 
        else:
            i += 1

    i = 0
    while i < len(calc_split):
        if calc_split[i] in ["+", "-"]:
            num1 = float(calc_split[i-1])
            num2 = float(calc_split[i+1])
            
            if calc_split[i] in ["+"]:
                op_result = Operations.add(num1, num2)
            else:
                op_result = Operations.substract(num1, num2)
            
            calc_split[i-1 : i+2] = [str(op_result)]
            i -= 1 
        else:
            i += 1
                
    result = calc_split[0]

    return result

def calc_result(calc_input, result):
    '''Function that take the result of the calcul and do the result message for the menu
    
    PARAMETERS -
    calc_input : the user input entered in the calcul
    result : the result of the calcul 
    
    RETURNS -
    result: return the result of the calcul for the menu to keep it in memory.'''
    if result == None:
        calc_input, result = calculator(result)
        print(f"{calc_input} is equal to {result}")
        time.sleep(0.2)
        input("Press enter to continue..")
        clear()
        return result
    else:
        previous_result = result

        calc_input, new_result = calculator(result)
        print(f"{previous_result} {calc_input} is equal to {new_result}")
        time.sleep(0.2)
        input("Press enter to continue..")
        clear()

        new_result = result

        return result


def erase_result(result):
    '''Function that erase the result memory to go back to a new calcul
    
    PARAMETERS -
    result : the result of the calcul 
    
    RETURNS -
    result: return the new result (None) for the menu to keep it in memory and reset.'''
    result = None
    print("The result has been reset !")
    time.sleep(0.2)
    input("Press enter to continue..")
    return result