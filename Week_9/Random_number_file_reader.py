#   FILE:   Random_number_file_reader.py
#   DATE:   2021-10-23
#   AUTHOR: Tyler Hand
#   DESCRIPTION:
"""
THis file is to show the sum of the numbers from the randomnumbers.txt and how many numbers it has in it.

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
    
    file_name = input('Please enter the file name: ')
    # Perform Processing
    count = 0
    total = 0 
    try: 
        in_file = open(file_name, 'r')
        for line in in_file:
            print(line.strip())
            value = int(line)
            count += 1
            total += value
    except FileNotFoundError as fnf:
        print(f'Cannot find file {file_name}')
    else: 
        print(f'Count is: {count}')
        print(f'Total is: {total}')
    finally:
        try:
            in_file.close()
        except:
            pass
    # Display the outputs
    
   
    # Let the use know the program is done
    print("\nProgram complete.\n")
   

# Call main()
if __name__ == "__main__":
    main(sys.argv)


