#   FILE:   Random_Number_File_Writer.py
#   DATE:   2021-10-19
#   AUTHOR: Tyler Hand
#   DESCRIPTION:
"""
Description of file goes here.

"""

import sys
import random

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
    program_title = "*** Random Number File Writer ***"
    print(f'\n{program_title:^{CONSOLE_WIDTH}}')
    # Get the inputs
    user_values = int(input('Enter number of values: '))
    # Perform Processing
    out_file = open('randomnumbers.txt', 'w')
    for line in range( user_values ):
        number = random.randint(1, 500)
        out_file.write(str(number)+ '\n')
    out_file.close()
    
    # Display the outputs
    
   
    # Let the use know the program is done
    print("\nProgram complete.\n")
   

# Call main()
if __name__ == "__main__":
    main(sys.argv)


