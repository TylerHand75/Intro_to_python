#   FILE:   Lo_Shu_Magic_Square.py
#   DATE:   2021-11-05
#   AUTHOR: Tyler hand
#   DESCRIPTION:
"""
Description of file goes here.

"""

import sys

# A constant for the number of characters across the console
CONSOLE_WIDTH = 80

a = [[4,9,2],[3,5,7],[8,1,6]]
def magic_square(a):
    for row in range(len(a)):
        total_row = 0
        for col in range(len(a)):
            total_row += a[row][col]
        if total_row != 15:
            return False

    for col in range(len(a)):
        total_column = 0
        for row in range(len(a)):
            total_column += a[col][row]
        if total_column != 15:
            return False

    total_right_diagonal = 0
    for i in range(len(a)):
        total_right_diagonal += a[i][i]
    if total_right_diagonal != 15:
        return False

    total_left_diagonal = 0
    for i in range(len(a),0,-1):
        total_left_diagonal += a[len(a)-i][i-1]
    if total_left_diagonal != 15:
        return False
    return True

def main(argv):
    """
    Description of main() goes here.

    INPUTS:
        argv A list of strings representing the command line arguments

    RETURNS:
        None
    """
    # Show the program title
    program_title = "*** Lo Shu magic square ***"
    print(f'\n{program_title:^{CONSOLE_WIDTH}}')
    print(magic_square(a))
   
    # Let the use know the program is done
    print("\nProgram complete.\n")
   

# Call main()
if __name__ == "__main__":
    main(sys.argv)


