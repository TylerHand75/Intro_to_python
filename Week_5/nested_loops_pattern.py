#   FILE:   nested_loops_pattern.py
#   DATE:   2021-09-28
#   AUTHOR: Tyler Hand
#   DESCRIPTION:
"""
this program is to make a upside down right triangle what a loop.

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
    program_title = "*** Nested Loops Pattern ***"
    print(f'\n{program_title:^{CONSOLE_WIDTH}}')
    
    for rows in range(7, 0 , -1 ):
        for column in range (rows, 0, -1):
            print("*", end = "", )
        print("")
    


    print("\nProgram complete.\n")
   

# Call main()
if __name__ == "__main__":
    main(sys.argv)

