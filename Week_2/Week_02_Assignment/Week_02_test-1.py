#   FILE:   Week_02_Assignment.py
#   DATE:   2021-09-06
#   AUTHOR: Tyler Hand
#   DESCRIPTION: This is the assignment for week_02
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
    
    program_title = "*** Week 2 Assingnment ***"
    print(f'\n{program_title:^{CONSOLE_WIDTH}}')

    # Get the inputs

    Name = input ("Please enter employee name: ")
    int1 = int(input("Please enter total number of widgets completed: ")) 
    int2 = number_of_total_widgets_a_box = 24 
    
    # Perform Processing

    print ("Program is Processing. ")
    int_sum = int1 // int2
    int3 = total_number_of_boxes = int_sum
    int4 = Left_over_widgets = int1 % int3 
    print("Processing Complete. ")

    # Display the outputs

    print('Name: ', Name)
    print('Number of boxes completed: ',  int3)
    print('Number of widgets left over:', int4)
     
    # Let the use know the program is done
    
    print("\nProgram complete.\n")
    print("Program End")


# Call main()
if __name__ == "__main__":
    main(sys.argv)
