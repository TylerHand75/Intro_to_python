#   FILE:   Item_counter.py
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
    program_title = "*** TITLE ***"
    print(f'\n{program_title:^{CONSOLE_WIDTH}}')
    # Get the inputs
    
    # Perform Processing
    try: 
        in_file = open('names.txt', 'r')
        name_count = 0 
        for line in in_file:
            name_count += 1 
        in_file.close()
        print(name_count)
    except Exception as err:
        print(err)
    
    # Display the outputs
    
   
    # Let the use know the program is done
    print("\nProgram complete.\n")
   

# Call main()
if __name__ == "__main__":
    main(sys.argv)


