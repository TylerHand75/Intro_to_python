#   FILE:   Week_03_Assignment_question_6.py
#   DATE:   2021-09-12
#   AUTHOR: Tyler Hand
#   DESCRIPTION: 
"""
this is the week_03_assignment_question_6.

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
    program_title = "*** Week 3 Assingnment quesiton 6  ***"
    print(f'\n{program_title:^{CONSOLE_WIDTH}}')
    # Get the inputs

    state_tax_title = 'State Tax'
    country_tax_title = 'Country Tax'
    purchase_amount = float(input('Please enter purchase amount:'))
    
    # Perform Processing


    bar = "-" * CONSOLE_WIDTH
    table_name = "Taxes"
    state_tax = purchase_amount*0.05
    country_tax = purchase_amount*0.025

    # Display the outputs

    print(f"\n{table_name: ^{CONSOLE_WIDTH}}")
    print(bar)
    print (f"\n | {state_tax_title:^15s} | {country_tax_title:^15s} | ")
    print(f' | {state_tax:<15f} | {country_tax:<15f} | ')
    print(bar) 

    # Let the use know the program is done
    print("Program Complete")
    print("End")
    

# Call main()
if __name__ == "__main__":
    main(sys.argv)