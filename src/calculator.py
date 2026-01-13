from src.operations import *

def calculator(result):

    delimiter = " "

    if result == "":
        calc_input = input("Write your calcul here...\n")
        calc_split = calc_input.split()
        result = operation_prio(calc_split)
        return calc_input, result

    else:
        calc_input = input(f"Current calcul : {result} ...\n")
        calc_split = calc_input.split()
        calc_split.insert(0, str(result))
        result = operation_prio(calc_split)
        return calc_input, result

def operation_prio(calc_split:list):

    for i, calc in enumerate(calc_split):
        if calc in ["x", "*", ":", "/"]:
            num1 = int(calc_split[i-1])
            num2 = int(calc_split[i+1])
            if calc == "x" or calc == "*":
                operation_result = multiply(num1, num2)
                calc_split[i] = str(operation_result)

                calc_split.remove(str(num1))
                calc_split.remove(str(num2))
            else : 
                operation_result = divide(num1, num2)
                calc_split[i] = str(operation_result)

                calc_split.remove(str(num1))
                calc_split.remove(str(num2))

    for i, calc in enumerate(calc_split):
        if calc in ["+", "-"]:
            num1 = int(calc_split[i-1])
            num2 = int(calc_split[i+1])
            if calc == "-":
                operation_result = substract(num1, num2)
                calc_split[i] = str(operation_result)

                calc_split.remove(str(num1))
                calc_split.remove(str(num2))
            else:
                operation_result = add(num1, num2)
                calc_split[i] = str(operation_result)

                calc_split.remove(str(num1))
                calc_split.remove(str(num2))
                
    result = calc_split[0]

    return result


