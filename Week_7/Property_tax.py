#   FILE:   Property_tax.py
#   DATE:   2021-10-10
#   AUTHOR: Tyler Hand
#   DESCRIPTION:
"""
this is a progeram to calculate proprerty tax

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
    program_title = "*** Property Tax ***"
    print(f'\n{program_title:^{CONSOLE_WIDTH}}')

    property_value = float(input("Please enter your Property Value:  "))    
    Your_property(property_value)
    
def Your_property (property_value):
    assessment_value = property_value * .6
    print("The assesnment of your home is ", (assessment_value))
    assessment(assessment_value)


def assessment (assessment_value):
    property_tax = assessment_value * .0072
    print("The property tax is ", (property_tax))
    
    

    print("\nProgram complete.\n")
   

# Call main()
if __name__ == "__main__":
    main(sys.argv)


