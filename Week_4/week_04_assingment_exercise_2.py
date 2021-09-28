#   FILE:   week_04_assingment_exercise_2.py
#   DATE:   2021-09-19
#   AUTHOR: Tyler Hand 
#   DESCRIPTION:
"""
This is the program to figure out which of the 2 triangles are bigger.

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
    program_title = "*** Areas of Rectangles ***"
    print(f'\n{program_title:^{CONSOLE_WIDTH}}')
    # Get the inputs

    length_1 = int(input('Please enter the length of the first triangle: '))
    width_1 = int(input('Please enter the width of the first triangle: '))
    length_2 = int(input('Please enter the length of the second triangle: '))
    width_2 = int(input('Please enter the width of the second triangle: '))
    
    # Perform Processing
    
    area_of_triangle_1 = length_1 * width_1
    area_of_triangle_2 = length_2 * width_2

    if area_of_triangle_1 < area_of_triangle_2:
        print('The area of the second triangle is greater.') 
    elif area_of_triangle_1 > area_of_triangle_2:
        print('The area of the first triangle is greater.') 
    else: 
        print('The area of the first triangle is equal the area of the second triangle')  
        
    
    # Display the outputs
   
    # Let the use know the program is done
    print("\nProgram complete.\n")
   

# Call main()
if __name__ == "__main__":
    main(sys.argv)


