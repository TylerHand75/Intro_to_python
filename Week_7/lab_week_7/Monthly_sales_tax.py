#   FILE:   Monthly_sales_tax.py
#   DATE:   2021_10_10
#   AUTHOR: Tyler Hand
#   DESCRIPTION:
"""
this is a program to show the monthly sales tax of the county and state.

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
    program_title = "*** Monthly sales tax ***"
    print(f'\n{program_title:^{CONSOLE_WIDTH}}')
    
    sales = float(input("Enter the total sales: "))
    displayTotals(sales)

def calculateStateTax(sales):
    state_tax = .05
    return sales * state_tax

def calculateCountyTax(sales):
    county_tax =  .025
    return sales * county_tax

def displayTotals(sales):
    state_tax = calculateStateTax(sales)
    print("The ammount of State tax is ", state_tax)
    county_tax = calculateCountyTax(sales)
    print("The ammount of County tax is ", county_tax)
    print("Total sales tax is ", state_tax + county_tax)


    print("\nProgram complete.\n")
   

# Call main()
if __name__ == "__main__":
    main(sys.argv)


