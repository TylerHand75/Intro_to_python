#   FILE:   Total_sales.py
#   DATE:   2021-10-29
#   AUTHOR: tyler hand
#   DESCRIPTION:
"""
Description of file goes here.

"""

import sys

# A constant for the number of characters across the console
CONSOLE_WIDTH = 80

def sales_total_sum(sales_list):
    total = 0
    for sale in sales_list:
        total += sale
    return total


def weekly_sales():
    sales = []
    for i in range(7):
        sales_day = float(input("Enter sales for day: " ))
        sales.append(sales_day)
    return sales


def main(argv):
    """
    Description of main() goes here.

    INPUTS:
        argv A list of strings representing the command line arguments

    RETURNS:
        None
    """
    # Show the program title
    program_title = "*** Toltal Sales ***"
    print(f'\n{program_title:^{CONSOLE_WIDTH}}')
    # Get the inputs
    
    sales = weekly_sales()
    total_weekly_sales = sales_total_sum(sales)
    print("The total weekly sales is $ "(total_weekly_sales))
    
    # Display the outputs
    
   
    # Let the use know the program is done
    print("\nProgram complete.\n")
   

# Call main()
if __name__ == "__main__":
    main(sys.argv)


