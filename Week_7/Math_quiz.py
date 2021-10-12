#   FILE:   Math_quiz.py
#   DATE:   2021-10-10
#   AUTHOR: <student name here>
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
    program_title = "*** Math Quiz ***"
    print(f'\n{program_title:^{CONSOLE_WIDTH}}')
    
    import random

    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100) 
    total = number1 + number2   
    print('\t', (number1))
    print('+\t', (number2)) 
    answer = additon(total)

def additon(answer):
    int(input("Please enter the answer: "))
    

def check(answer, total):
    if answer == total:
        print("Congradulations ")
    else:
        print("The answer is ", total)

    check(answer, total)


    print("\nProgram complete.\n")
   

# Call main()
if __name__ == "__main__":
    main(sys.argv)


