#   FILE:   Grader.py
#   DATE:   2021-09-14 
#   AUTHOR: Gaddis 
#   DESCRIPTION:
"""
examples from pages 130 through 132 of the gaddis text

this program gets a numeric test score from the user and displays the corrospinding letter grade. 

"""

import sys

# A constant for the number of characters across the console
CONSOLE_WIDTH = 80
#name constance to reporesent the grade threshold
A_score = 90
B_score = 80
C_score = 70 
D_score = 60 

def main(argv):
    """
    Description of main() goes here.

    INPUTS:
        argv A list of strings representing the command line arguments

    RETURNS:
        None
    """
    # Show the program title
    program_title = "*** Grader ***"
    print(f'\n{program_title:^{CONSOLE_WIDTH}}')
    # Get the inputs
    score = int(input("Enter your test score: "))

    # determain the grade and display the output 
    # skip to page 132 
    if  score >= A_score:
        print('Your grade is A. ')
    elif score >= B_score:
        print('Your grade is B. ')
    elif score >= C_score:
        print('Your grade is C. ')
    elif score >= D_score:
        print('Your grade is D. ')
    else:
        print('Your Grade is F. ')
    # Let the use know the program is done
    print("\nProgram complete.\n")
   

# Call main()
if __name__ == "__main__":
    main(sys.argv)


