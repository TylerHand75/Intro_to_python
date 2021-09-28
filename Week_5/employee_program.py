#   FILE:   employee_program.py
#   DATE:   2021-09-23
#   AUTHOR: Tyler Hand 
#   DESCRIPTION:
"""
The week 5 program for th eemployee program. we have added a loop for the menu so that it pepeats untill the user says to quit.

This is the second lab for the emplyee lab example. learning to do a menu. 
This example will grow as we cover new concepts during the semester.

Note: users like to enter numbers for menu choices, but we arnt using the numbers for math. 
This means we can treat the numbers as strings, without attemptingto convert the to an int. 

"""

import sys

# A constant for the number of characters across the console
CONSOLE_WIDTH = 80

# Inputs
# user_choice string from the user 
# Processes 
# Show the program title
# Show the menu
# prompt the user for a choice and read that choice 
# show a message based on the users choice 
# ask the user to press Enter to continue 
# show program is complete
# Outputs
# A message discribing the users choice or an error message



def main(argv):
    """
    this function will print a menu of options for the user. then it will ask for the user's choice. 
    it will print the user's choice. it will print an error message if the choice is not a valid options. 

    INPUTS:
        argv A list of strings representing the command line arguments

    RETURNS:
        None
    """
    # Show the program title
    program_title = "*** Employee program ***"
    print(f'\n{program_title:^{CONSOLE_WIDTH}}')
    #define the loop variable.
    done = False
    #deinfe the prompt 
    prompt = '\n Your choice: '
    # Start the loop
    while not done:  
        # Print the menu
        print('\t-- Main Menu --')
        print('\t1) Add an Employee')
        print('\t2) Show all Employees')
        print('\t3) View an Employee')
        print('\t4) Update an Employee')
        print('\t5) Delete an Employee')
        print('\tQ) Quit')

        # Get the inputs
        prompt = '\n Your choice:'
        user_choice = input(prompt)

        #decide what to do based on the user choice
        if user_choice == '1':
            print('\nYou chose to Add and Employee record.')
        elif user_choice == '2':
            print('\nYou chose to show all Employee records.')
        elif user_choice == '3':
            print('\nYou chose to view an Employee record.')
        elif user_choice == '4':
            print('\nYou chose to Update an Employee record.')
        elif user_choice == '5':
            print('\nYou chose to Delete an Employee record.')
        elif user_choice == 'Q' or user_choice == 'q':
            print('\nYou chose to Quit.')
            done = True
        else: 
            print('\nYour choice was not recognized. Please try again.')
        
        # Tell the user to press Enter to continue
        input('\n Press the Enter Key to continue:')
    
    # Let the use know the program is done
    print("\nProgram complete.\n")
   

# Call main()
if __name__ == "__main__":
    main(sys.argv)

