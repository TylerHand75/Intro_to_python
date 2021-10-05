#   FILE:   Compound_intrest.py
#   DATE:   2021-09-12
#   AUTHOR: Tyler Hand
#   DESCRIPTION: 
"""
this is the week_03_assignment_question_14.

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
    program_title = "*** Compound_intrest  ***"
    print(f'\n{program_title:^{CONSOLE_WIDTH}}')
    # Get the inputs

    original_prompt = "Please enter the original amount deposited into account: "
    annual_interest_prompt = "Please enter the annual interest rate: "
    compounded_prompt = "Please enter the numbers of times it is compouneded a year: "
    number_of_years_prompt = "Please enter the numbers of years account will gain interest: "

    original = int(input(original_prompt))
    annual = float(input(annual_interest_prompt))
    compounded = int(input(compounded_prompt))
    years = int(input(number_of_years_prompt))
    
    
    # Perform Processing


    total_amount_gained = original * ((1 + (annual/ (100.0 * compounded))) ** (compounded * years))
    
    bar = "-" * CONSOLE_WIDTH
    table_name = "Money made from Interest"
    
    # Display the outputs

    print(f"\n{table_name: ^{CONSOLE_WIDTH}}")
    print(bar)
    print (f"\n | {table_name:^15s} | ")
    print(f' | {total_amount_gained:<24f} | ')
    print(bar) 

    # Let the use know the program is done
    print("Program Complete")
    print("End")
    

# Call main()
if __name__ == "__main__":
    main(sys.argv)