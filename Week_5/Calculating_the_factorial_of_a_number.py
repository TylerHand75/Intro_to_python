#   FILE:   Calculating_the_factorial_of_a_number.py
#   DATE:   <date here in ISO-8601 format>
#   AUTHOR: <student name here>
#   DESCRIPTION:
"""
Description of file goes here.

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
    program_title = "*** Calculating the factorial of a number ***"
    print(f'\n{program_title:^{CONSOLE_WIDTH}}')
    
    user_integer = int(input("Please enter a number: "))
    factorial = 1


    while user_integer < 1:
        user_integer = int(input("Please enter a Positive number: "))
    
    for number in range(1, user_integer + 1):
        factorial = factorial * number

    print("\nThe factorials of ", str(user_integer), " is " , str(factorial) )

    print("\nProgram complete.\n")
   

# Call main()
if __name__ == "__main__":
    main(sys.argv)

