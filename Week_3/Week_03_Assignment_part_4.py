#   FILE:   Week_03_Assignment_question_9.py
#   DATE:   2021-09-12
#   AUTHOR: Tyler Hand
#   DESCRIPTION: 
"""
this is the week_03_assignment_question_9.

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
    program_title = "*** Week 3 Assingnment question 9  ***"
    print(f'\n{program_title:^{CONSOLE_WIDTH}}')
    # Get the inputs

    celsius_prompt = "Please enter Celsius Temperature: "
    celsius = float(input(celsius_prompt))
    
    # Perform Processing

    convert_temp = 9/5 * celsius + 32
    bar = "-" * CONSOLE_WIDTH
    table_name = "Fahrenheit Temperature"
    
    # Display the outputs

    print(f"\n{table_name: ^{CONSOLE_WIDTH}}")
    print(bar)
    print (f"\n | {table_name:^15s} | ")
    print(f' | {convert_temp:<22f} | ')
    print(bar) 

    # Let the use know the program is done
    print("Program Complete")
    print("End")
    

# Call main()
if __name__ == "__main__":
    main(sys.argv)