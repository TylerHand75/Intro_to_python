#   FILE:   Calories_burned.py
#   DATE:   2021-09-23
#   AUTHOR: Tyler Hand
#   DESCRIPTION:
"""
Programming exercise 2 of the gaddis text on plag 203.

"""

import sys
# inputs: 
#	none
# processes:
#-	define variables
#	- 4.2 calories per minutes
#	- starting minutes = 10 
#	- ending minutes = 30
#	- step = 5 
#-	Print the header
#-	loop throught minutes
#	- calculate calories
#	- print calories and minutes
#- show program complete
# Outputs:
#-	table header
#-	calories burned
#-	minutes
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
    program_title = "*** Calories Burned ***"
    print(f'\n{program_title:^{CONSOLE_WIDTH}}')
    # declaire varibles 
    calories_per_min = 4.2
    start = 10 
    end = 30 
    step = 5 

    
    # Display the table header
    print('minute\t calories')
    for minutes in range(start, end + 1 , step):
        calories = minutes * calories_per_min
        print(f'{minutes}\t{calories:>6.1f}')

    
    # Display the outputs
    
   
    # Let the use know the program is done
    print("\nProgram complete.\n")
   

# Call main()
if __name__ == "__main__":
    main(sys.argv)


