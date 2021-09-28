#   FILE:   Population.py
#   DATE:   2021-09-28
#   AUTHOR: Tyler Hand 
#   DESCRIPTION:
"""
This program is to simutlate the the Population of organisms. 

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
    program_title = "*** Population ***"
    print(f'\n{program_title:^{CONSOLE_WIDTH}}')
    # inputs
    starting_Number = int(input("Enter the Starting number of organisms: "))
    Daily_increase = float(input("Enter the average daily increase: "))
    number_of_days = int(input("Enter the number of days to multiply: "))
    Daily_increase = Daily_increase / 100
    
    # Process 
    print(f"\nDays\t Approximate Population ")
    for today in range(1, number_of_days + 1):
        print(today, "\t",starting_Number )
        starting_Number = starting_Number + (Daily_increase * starting_Number)


    print("\nProgram complete.\n")
   

# Call main()
if __name__ == "__main__":
    main(sys.argv)

