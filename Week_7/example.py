#   FILE:   Example_week_7.py
#   DATE:   2021-10-5
#   AUTHOR: Tyler Hand
#   DESCRIPTION:
"""
Demonstating using moduals. 
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
    program_title = "*** Example of modual ***"
    print(f'\n{program_title:^{CONSOLE_WIDTH}}')
    # Get the inputs


    name = ui_helper.get_user_string("Please enter Your Name: ")



    # Perform Processing
    
    
    # Display the outputs
    
   
    # Let the use know the program is done
    print("\nProgram complete.\n")
   

# Call main()
if __name__ == "__main__":
    main(sys.argv)


