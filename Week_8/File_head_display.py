#   FILE:   File_head_dispaly.py
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
    program_title = "*** File head display ***"
    print(f'\n{program_title:^{CONSOLE_WIDTH}}')
    # Get the inputs
    file_name = input("Please enter the file name: ")
    try: 
        in_file = open(file_name, 'r')
        line_count = 0 
        for line in in_file:
            print(line.strip())
            line_count += 1 
            if line_count > 4:
                break
    except Exception as err:
            print(err)
    finally:
        try: 
            in_file.close()
        except:
            pass 
    # Perform Processing
    
    
    # Display the outputs
    
   
    # Let the use know the program is done
    print("\nProgram complete.\n")
   

# Call main()
if __name__ == "__main__":
    main(sys.argv)


