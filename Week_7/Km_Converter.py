#   FILE:   Km_converter.py
#   DATE:   2021-09-28
#   AUTHOR: Tyler hand 
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
    program_title = "*** Km Converter ***"
    print(f'\n{program_title:^{CONSOLE_WIDTH}}')
    # Get the inputs

    km = get_kilometers()
    miles = convert(km)
    display_miles(miles)

    print("\nProgram complete.\n")

def get_kilometers():
    """
    ask the user for the distance in km
    returns: 
        kilometers float
    """
    get_kilometers = float(input("please enter the distance in kilometers:"))
  
    return get_kilometers

def convert(km):

    return km * 0.6214

def display_miles(miles):
    print(f'This is {miles:.2f} miles.')


# Call main()
if __name__ == "__main__":
    main(sys.argv)

