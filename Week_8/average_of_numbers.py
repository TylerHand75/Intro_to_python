#   FILE:   average_of_numbers.py
#   DATE:   2021-10-19
#   AUTHOR: Tyler Hand
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
    program_title = "*** Average of Numbers ***"
    print(f'\n{program_title:^{CONSOLE_WIDTH}}')
    
    # Perform Processing
    
    in_file = open('numbers.txt', 'r')
    ammount= 0
    total = 0
    for line in in_file:
        ammount += int(line)
        total += 1
        average = (ammount/total)
    print(average)
    in_file.close()
    # Display the outputs
    
   
    # Let the use know the program is done
    print("\nProgram complete.\n")
   

# Call main()
if __name__ == "__main__":
    main(sys.argv)


