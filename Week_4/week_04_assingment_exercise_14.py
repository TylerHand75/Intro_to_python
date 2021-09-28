#   FILE:   week_04_assingment_exersise_14.py
#   DATE:   2021-09-19
#   AUTHOR: Tyler Hand
#   DESCRIPTION:
"""
this program is to show your bmi and tell you if you are unvder or over weight.

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
    program_title = "*** TITLE ***"
    print(f'\n{program_title:^{CONSOLE_WIDTH}}')
    # Get the inputs
    weight = float(input('Please enter your weight in pounds:'))
    height = float(input('Please enter your height in inches:'))
    # Perform Processing
    bmi = weight * 703 / (height ** 2)

    if bmi < 18.5: 
        print('Your body mass index is', format(bmi, '.2f'), 'You are Under weight')
    elif bmi > 25:
        print('Your body mass index is', format(bmi, '.2f'), 'You are Over weight')
    else:
        print('Your body mass index is', format(bmi, '.2f'), 'You are Optimal weight')

    
    # Display the outputs
    
   
    # Let the use know the program is done
    print("\nProgram complete.\n")
   

# Call main()
if __name__ == "__main__":
    main(sys.argv)


