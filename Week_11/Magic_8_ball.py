#   FILE:   Magic_8_ball.py
#   DATE:   2021-11-06
#   AUTHOR: Tyler hand 
#   DESCRIPTION:
"""
Description of file goes here.

"""
import random
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
    program_title = "*** Magic 8 ball  ***"
    print(f'\n{program_title:^{CONSOLE_WIDTH}}')

    infile = open('8_ball_responses.txt','r')
    responses = infile.readlines()
    for i in range(len(responses)):
        responses[i] = responses[i].rstrip('\n')
    question = input("Enter a question: ")
    print(responses[random.randint(0,len(responses)-1)])
    infile.close()



    # Let the use know the program is done
    print("\nProgram complete.\n")
   

# Call main()
if __name__ == "__main__":
    main(sys.argv)


