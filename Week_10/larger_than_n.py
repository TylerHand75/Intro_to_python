#   FILE:   larger_than_n.py
#   DATE:   2021-10-28
#   AUTHOR: Tyler hand
#   DESCRIPTION:
"""
Description of file goes here.

"""
import random
import sys

# A constant for the number of characters across the console
CONSOLE_WIDTH = 80


def bigger_than(n, list_a):
    """
    returns a list of all the values in list_a athat are larger than n
    """
    new_list = []
    for value in list_a:
        if value > n:
            new_list.append(value)
    return new_list


def main(argv):
    """
    Description of main() goes here.

    INPUTS:
        argv A list of strings representing the command line arguments

    RETURNS:
        None
    """
    # Show the program title
    program_title = "*** larger than N ***"
    print(f'\n{program_title:^{CONSOLE_WIDTH}}')
    # random numbers
    
    min_number = 1
    max_number = 500
    size = 20
    n = random.randint(min_number, max_number)
    the_list = []
    for x in range(size):
        the_list.append(random.randint(min_number, max_number))
    print(n)
    print(the_list)

    # Perform Processing
    larger = bigger_than(n,the_list)
    
    # Display the outputs
    print(larger)
    
   
    # Let the use know the program is done
print("\nProgram complete.\n")
   

# Call main()
if __name__ == "__main__":
    main(sys.argv)


