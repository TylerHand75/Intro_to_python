#   FILE:   week_04_assingment_exercise_9.py
#   DATE:   2021-09-19
#   AUTHOR: Tyler Hand
#   DESCRIPTION:
"""
this program is to figure out what color a pocket is.

"""

import sys

# A constant for the number of characters across the console
CONSOLE_WIDTH = 80

def main(argv):
    """
    Description of main() goes here.

    INPUTS:
        argv A list of strings representing the command line arguments

    RETURNS:
        None
    """
    # Show the program title
    program_title = "*** Roylette Wheel Color ***"
    print(f'\n{program_title:^{CONSOLE_WIDTH}}')
    # Get the inputs

    number = int(input('Please enter a pocket number: '))

    if number == 0:
        print('green')

    elif number >=1 and number <= 10:
        if number % 2!= 0:
            print('Red')
        else:
            print('Black')
    elif number >= 11 and number <= 18:
        if number % 2 != 0:
            print('Black')
        else:
            print('Red')
    elif number >= 19 and number <= 28:
        if number % 2 != 0:
            print('Red')
        else:
            print('Black')
    elif number >= 29 and number <= 36:
        if number % 2 != 0:
            print('Black')
        else:
            print('Red')
    else: 
        print('Error Invalid Number.')
    # Let the use know the program is done
    print("\nProgram complete.\n")
   

# Call main()
if __name__ == "__main__":
    main(sys.argv)


