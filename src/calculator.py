from src.operations import *

def calculator():
    usr_input = input("Write your calcul here...\n")
    calc_split = usr_input.split()

    for calc in calc_split:
        if calc == "x" or calc == "*" or calc == "/" or calc == ":":
            num1 = calc_split[calc-1]
            num2 = calc_split[calc+1]
            if calc == "x" or calc == "*":
                calc_split[calc] = multiply(num1, num2)
            else : 
                calc_split[calc] = divide(num1, num2)
        
    for calc in calc_split:
        if calc == "-" or calc == "+":
            num1 = calc_split[calc-1]
            num2 = calc_split[calc+1]
            if calc == "-":
                calc_split[calc] = substract(num1, num2)
            else:
                calc_split[calc] = add(num1, num2)







