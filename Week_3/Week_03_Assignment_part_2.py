#   FILE:   Week_03_Assignment_part_2.py
#   DATE:   2021-09-12
#   AUTHOR: Tyler Hand
#   DESCRIPTION: 
"""
this is the week_03_assignment_part_2.

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
    program_title = "*** Week 3 Assingnment part 2  ***"
    print(f'\n{program_title:^{CONSOLE_WIDTH}}')
    # Get the inputs
    bar = "-" * CONSOLE_WIDTH
    table_name = "Distances" 
    # Perform Processing
    distance_in_6_hours_title = "Distance in 6 Hours"
    distance_in_10_hours_title = "Distance in 10 Hours"
    distance_in_15_hours_title = "Distance in 15 Hours"
    distance_in_6_hours = 70 * 6
    distance_in_10_hours = 70 * 10
    distance_in_15_hours = 70 * 15

    # Display the outputs
    print(f"\n{table_name: ^{CONSOLE_WIDTH}}")
    print(bar)
    print (f"\n | {distance_in_6_hours_title} | {distance_in_10_hours_title} | {distance_in_15_hours_title} |")
    print(f'| {distance_in_6_hours} | {distance_in_10_hours} | {distance_in_15_hours} | ')
    print(bar) 
    # Let the use know the program is done
    
    

# Call main()
if __name__ == "__main__":
    main(sys.argv)