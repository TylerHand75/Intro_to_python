#   FILE:   Word_Frequency.py
#   DATE:   11-30-2021
#   AUTHOR: Tyler hand 
#   DESCRIPTION:
"""
Description of file goes here.

"""

import sys

# A constant for the number of characters across the console
CONSOLE_WIDTH = 80
FILE_NAME = 'words.txt'
def main(argv):
    """
    Description of main() goes here.

    INPUTS:
        argv A list of strings representing the command line arguments

    RETURNS:
        None
    """
    # Show the program title
    program_title = "*** Word Frequency ***"
    print(f'\n{program_title:^{CONSOLE_WIDTH}}')
    # Get the inputs
    text_file = {}
    # Perform Processing
    words = FILE_NAME.split()
    for word in words:
        if word not in text_file:
            text_file[word] = 0
        text_file[word] +=1 
    return text_file
    
    # Display the outputs
    
   
    # Let the use know the program is done
    print("\nProgram complete.\n")
   

# Call main()
if __name__ == "__main__":
    main(sys.argv)


