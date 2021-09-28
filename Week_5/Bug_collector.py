#   FILE:   Bug_collector.py
#   DATE:   2021-09-26
#   AUTHOR: Tyler Hand
#   DESCRIPTION:
"""
this program is to calculate the total numbers of bugs that you collected.

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
    program_title = "*** Bug Collector ***"
    print(f'\n{program_title:^{CONSOLE_WIDTH}}')
    # get the number of bugs
    total_bugs = 0
    total_days = 5
    # the process
    for current_day in range(1, total_days + 1):
        bugs_collected = int(input("How many bugs were collected on day " + str(current_day) + " : "))
        total_bugs += bugs_collected

    #display outputs
    print("The number of total bugs collected in 5 days is " + str(total_bugs) + ".")

    print("\nProgram complete.\n")


# Call main()
if __name__ == "__main__":
    main(sys.argv)
