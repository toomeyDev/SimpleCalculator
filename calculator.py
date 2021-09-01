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
    print("Choose an operation (addition, subtraction, multiplication, division)\n")
    ans = None
    valid_operations = ["addition","subtraction","multiplication","division"]
    while ans == None: 
        ans = input("Choice: ")
        if ans in valid_operations:
            # if ans is a valid operation, match to corresponding function in operations
            operation = getattr(operations, ans)
            n1 = int(input(f"Performing {ans}, choose first number: \n"))
            n2 = int(input(f"Choose second number: \n"))
            answer = operation(n1, n2)
            print(f"Result is: {answer}")
            exit_query = input("Perform more operations? (y/n)\n").lower()
            if exit_query == 'y':
                ans = None
                sleep(1)
                clear_screen()
            elif exit_query == 'n':
                sleep(1)
                clear_screen()
                break
            else:
                print("Expecting y or n, defaulting to n.")
                sleep(1)
                clear_screen()
        else:
            # if ans is not a valid operation, continue asking for input    
            ans = None

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
