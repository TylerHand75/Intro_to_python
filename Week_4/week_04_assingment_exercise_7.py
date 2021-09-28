#   FILE:   week_04_assingment_exersise_7.py
#   DATE:   2021-09-19
#   AUTHOR: Tyler Hand
#   DESCRIPTION:
"""
This is a program to help with mixing primary colors.

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
    program_title = "*** Color Maker ***"
    print(f'\n{program_title:^{CONSOLE_WIDTH}}')
    # Get the inputs

    User_color_1 = input('Please enter your first color? (red, blue, yellow) :')
    User_color_2 = input('Please enter your second color? (red, blue, yellow) :')

    red = 'red'
    blue = 'blue'
    yellow = 'yellow'

    # Perform Processing

    if User_color_1 == red and User_color_2 == blue or User_color_1 == blue and User_color_2 == red: 
        print('\nPurple')
    elif User_color_1 == red and User_color_2 == yellow or User_color_1 == yellow and User_color_2 == red:
        print('Orange')
    elif User_color_1 == blue and User_color_2 == yellow or User_color_1 == yellow and User_color_2 == blue:
        print('Green')
    else: 
        print('Invalid Color')    


    # Display the outputs
    
   
    # Let the use know the program is done
    print("\nProgram complete.\n")
   

# Call main()
if __name__ == "__main__":
    main(sys.argv)


