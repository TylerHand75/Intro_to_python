#   FILE:   Budget_analsis.py
#   DATE:   2021-09-26
#   AUTHOR: Tyler Hand
#   DESCRIPTION:
"""
This is program to calculate your budgeting for the month

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
    program_title = "*** Budget Analsis ***"
    print(f'\n{program_title:^{CONSOLE_WIDTH}}')

    cost = 0.0
    budget = 0.0
    difference = 0.0
    total_expense = 0
    keep_going = 'y'


    #Inputs
    budget = float(input("What is your budget for the month: "))
    print("Please begin entering the amounts of each of your monthly expenses: ")

    while keep_going == 'y':
        cost = float(input("How much have you spent: $"))
        total_expense = total_expense + cost
        keep_going = input("Have you spent any more: (Enter y for yes.)")

    if cost <= budget:
        difference = budget - cost
        print("You were $", difference, " under budget.")

    elif cost >= budget:
        difference = cost - budget
        print("You were $", difference, " over budget.")

    else:
        print("On budget. ")


    input("Press enter to exit.")

# Display the outputs


print("\nProgram complete.\n")


# Call main()
if __name__ == "__main__":
    main(sys.argv)
