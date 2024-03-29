#   FILE:   Sum_of_numbers..py
#   DATE:   2021-09-26
#   AUTHOR: Tyler Hand
#   DESCRIPTION:
"""
This is a program to calculate the sum of numbers in a loop.

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
    program_title = "*** Sum of numbers ***"
    print(f'\n{program_title:^{CONSOLE_WIDTH}}')
    
    user_number = float(input("Please enter the first number or a negative number to Quit: "))
    total = 0 

    while user_number > -1:
        total = total + user_number
        user_number = float(input("Please enter the next number or a negative number to Quit: "))

    print("\nThe sum of all your numbers is " + str(total))


    print("\nProgram complete.\n")
   

# Call main()
if __name__ == "__main__":
    main(sys.argv)

