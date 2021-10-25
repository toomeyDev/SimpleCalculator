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


def menu():
    operators = ['+','-','/','%','*'] # store valid operators
    
    # prompt for input
    user_input = input("Enter an operation (IE: '5 + 10')\n"
    +"any detected valid operations will be executed.\n")

    # parse valid numbers and operators from input
    operation_stream = [] # store valid numbers and operators
    for i in range(0, len(user_input)):
        if user_input[i].isnumeric():
            # if an integer is detected, parse and add to stream
            operation_stream.append((int)(user_input[i]))
        if user_input[i] in operators:
            operation_stream.append(user_input[i])
    print(operation_stream) # for testing

        

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
