import operations
import os
from time import sleep
"""
Central file for sequencing and user input associated with
the calculator. Takes in numbers, choices from user and
executes associated operations returning the results to terminal.
"""

def intro():
    print("Welcome to calculator, a simple command line utility for\n"
    + "performing basic arithmetic within the terminal.\n")
    ans = None
    while ans != '':
        ans = input("Press enter to continue: \n")


def perform_operation(operand_a = None, operator = None, operand_b = None):
    output = 0

    # if three non-None values aren't present, return None
    if operand_a == None or operand_b == None or operator == None:
        return None

    if operator == '+':
        output = operations.addition(operand_a, operand_b)
    elif operator == '-':
        output = operations.subtraction(operand_a, operand_b)
    elif operator == '*':
        output = operations.multiplication(operand_a, operand_b)
    elif operator == '/':
        output = operations.division(operand_a, operand_b)
    return output

# requires fixing
def execute_operation_stream(stream): 
    ops = []
    for item in stream:
        ops.append(item)
        if len(ops) == 3:
            ops_result = perform_operation(ops[0], ops[1], ops[2])
            ops.clear()
            ops.append(ops_result)
    return(ops[0]) # return final result
            
        
def menu():
    operators = ['+','-','/','%','*'] # store valid operators
    
    # prompt for input
    user_input = input("Enter an operation (IE: '5 + 10')\n"
    +"any detected valid operations will be executed.\n")
    user_input = user_input.split()

    operation_stream = [] # store valid numbers and operators
    for item in user_input:
        # parse valid numbers and operators from input
        if item.isnumeric():
            operation_stream.append(int(item))
        elif item in operators:
            operation_stream.append(item)

    result = execute_operation_stream(operation_stream)
    print(f"Result is {result}")
    

def main():
    intro()
    menu()


def clear_screen():
    """Clear the terminal/console of any generated text."""
    # make use of 'cls' command to clear screen in Windows
    if os.name == 'nt':
        os.system('cls')
    # use 'clear' for all other operating systems (linux, macosx etc)
    else:
        os.system('clear')

if __name__ == '__main__':
    main()
