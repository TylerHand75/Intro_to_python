#   FILE:   Week_02_lab.py
#   DATE:   2021-09-02
#   AUTHOR: Tyler hand
#   DESCRIPTION: This is the week_02_lab
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
    program_title = "*** TITLE ***"
    print(f'\n{program_title:^{CONSOLE_WIDTH}}')
    # Get the inputs

    name = input ("please enter your name: ")
    int1 = int(input("Please enter the first integer: "))
    int2 = int(input("Please enter the second integer: "))
    int3 = int(input("Please enter the third integer: "))
    float1 = float(input("Please enter the first floating point number: "))
    float2 = float(input("Please enter the second floating point number: "))
    float3 = float(input("Please enter the third floating point number: "))
    # Perform Processing
    print ("Program is processing: ")
    number_of_int_values = 3
    number_of_float_values = 3
    int_sum = int1 + int2 + int3
    int_avg = int_sum / 3 
    float_sum = float1 + float2 + float3
    float_avg = float_sum / 3
    print("Procesing is Complete: ") 
    # Display the outputs
    print("Thank you for your input: ", name)
    print(int_sum)
    print(int_avg)
    print(float_sum)
    print(float_avg)
    print("Procesing is Complete: ") 
    # Let the use know the program is done
    print("\nProgram complete.\n")


# Call main()dw
if __name__ == "__main__":
    main(sys.argv)


