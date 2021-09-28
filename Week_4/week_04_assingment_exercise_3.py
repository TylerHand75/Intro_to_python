#   FILE:   week_04_assingment_exercise_3.py
#   DATE:   2021-09-19 
#   AUTHOR: Tyler Hand
#   DESCRIPTION:
"""

this program is to determain i the person is a infant or a child or a teenager or an adult.
this is exercise 3  

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
    program_title = "*** Age clasifier ***"
    print(f'\n{program_title:^{CONSOLE_WIDTH}}')

    age = int(input('Please enter your age:'))
    
    # the outputs
    if  age <= 1:
        print('\nYou are an infant. ')
    elif age > 1 and age< 13:
        print('\nYou are a child. ')
    elif age >=13 and age < 20:
        print('\nYou are a teenager. ')
    else:
        print('\nYou are an adult. ')
    
    # Let the use know the program is done
    print("\nProgram complete.\n")
   

# Call main()
if __name__ == "__main__":
    main(sys.argv)


