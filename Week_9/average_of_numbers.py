#   FILE:   average_of_numbers.py
#   DATE:   2021-10-24
#   AUTHOR: Tyler Hand
#   DESCRIPTION:
"""
this is a continuation of exerise 6 from last week adding exceptions.

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
    try:
        in_file = open('numbers.txt', 'r')
        ammount= 0
        total = 0
        for line in in_file:
            ammount += int(line)
            total += 1
            average = (ammount/total)
        print(average)
    except FileNotFoundError as fnf:
        print(fnf)
    except ValueError as ve:
        print(ve)
    except Exception as ex:
        print(ex)
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


