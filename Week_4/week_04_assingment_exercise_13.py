#   FILE:   week_04_assingment_exersise_13.py
#   DATE:   2021-09-19
#   AUTHOR: Tyler Hand
#   DESCRIPTION:
"""
this programis to show shipping charges.

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
    program_title = "*** Shipping Charges ***"
    print(f'\n{program_title:^{CONSOLE_WIDTH}}')
    # Get the inputs
    weight = int(input('Please enter the weight of the package: '))
    # Perform Processing
    
    if weight < 2:
        print('Shipping will cost $1.50.')
    elif weight > 2 and weight < 6:
        print('Shipping will cost $3.00.')
    elif weight > 6 and weight < 10:
        print('Shipping will cost $4.00.')
    else:
        print('Shipping wil cost $4.50.')
    # Display the outputs
    
   
    # Let the use know the program is done
    print("\nProgram complete.\n")
   

# Call main()
if __name__ == "__main__":
    main(sys.argv)


