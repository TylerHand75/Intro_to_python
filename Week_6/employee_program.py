#   FILE:   employee_program.py
#   DATE:   2021-09-30
#   AUTHOR: Tyler Hand
#   DESCRIPTION:
"""
The week 6 program for the employee program.
we will add functions and comandline arguments.

This is the Third lab for the emplyee lab example. learning to do a menu.
This example will grow as we cover new concepts during the semester.

Note: users like to enter numbers for menu choices,
but we arnt using the numbers for math.
This means we can treat the numbers as strings,
without attemptingto convert the to an int.

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
    this function will print a menu of options for the user.
    then it will ask for the user's choice.
    it will print the user's choice.
    it will print an error message if the choice is not a valid options.

    INPUTS:
        argv A list of strings representing the command line arguments

    RETURNS:
        None
    """
    do_program_logic()

    # Let the use know the program is done
    print("\nProgram complete.\n")

# #############################################################################
# functions to respond to the comand line elements arguments
# #############################################################################


def do_program_logic():
    """
    this is the primanry programing logic implmenting the menu.
    it repersents the primarty starting point for the comon use of this program
    """
    program_title = 'Employee Program'
    show_program_title(program_title, CONSOLE_WIDTH)
    done = False
    invalid_option_message = "Your choice was not recognized. Try again."
    while not done:
        user_choice = get_user_choice()
        if user_choice == '1':
            add_employee()
        elif user_choice == '2':
            show_all_employees()
        elif user_choice == '3':
            view_employees_records()
        elif user_choice == '4':
            Update_an_Employee_record()
        elif user_choice == '5':
            Delete_an_Employee_record()
        elif user_choice == 'Q' or user_choice == 'q':
            done = confirm_quit()
        else:
            print(invalid_option_message)


# #############################################################################
# menu functions
# #############################################################################

def get_user_choice():
    """
        display the menu and ask the user to do something 
       Returns:
            string user's choice
    """
    menu_title = 'Main Menu'
    prompt = "Your choice: "
    options = ['1) Add an employee ','2) show all employee ',
    '3) view employee records ','4) update an employee record ',
    '5) delete an employee record ','6) Quit ']
    show_menu(menu_title,options)
    return get_user_string(prompt)


def show_menu(menu_title,options):
    """
        display a menu un a stuctured format
        input: 
        menu_title a string with the title of a menu 
        Optionsa list containing strings for the menu
    """
    print(f'\n\n\t--{menu_title}--')
    for option in options:
        print(f'\t {option}')

def get_user_string(prompt):
        """
            prompts the user to enter a string and returns the string
        """
        return input(prompt)

def  confirm_quit():
    """
        displpay a message stating the user has chosen to Quit
        ask the user to confirm by entering Y or N. if the user enters
        Y or y the return True
    """ 
    print('You Chose to Quit')
    choice = get_user_string('Confirm (Y/N)')
    return choice == 'Y' or choice == 'y'

# #############################################################################
# Function for general user interaction
# these functions separate the view logic from the control and model logic.
# #############################################################################

def show_program_title(title,WIDTH):
    """Displays the program title in a consitent manor 

    inputs: title sting with the title of the program 
    width the width of the screen, used for centering.
    """
    new_title='*** ' + title.upper() + ' ***'
    print(f'\n{new_title:^{WIDTH}}')


def show_section_title(title):
    """
        displays tehh section title in a consistant format
    inputs:
        titel string conatining the title text of the section
    """
    print(f'\n\t-- {title}--')


def press_enter_to_continue():
    """
        display a message telling the user to press the Enter key to continue
        Wait untill they do. ignore anything else they enter.    
    """
    input('\nPress the Enter key to continue...')

# #############################################################################
# employee handiling functions
# these are the functions for working with employee records
# #############################################################################


def add_employee():
    """
        handles all the logic for adding an employee record
    """
    show_section_title('Add an employee')
    print('\n You chose to enter an new employee record.')
    press_enter_to_continue()


def show_all_employees():
    """
        handles all the logic for showing all employees
    """
    show_section_title('Show all employees')
    print('\n You chose to enter Show all employees.')
    press_enter_to_continue()


def view_employees_records():
    """
        handles all the logic for viewing an employee record
    """
    show_section_title('View employees records')
    print('\n You chose to enter View employees records.')
    press_enter_to_continue()


def Update_an_Employee_record():
    """
        handles all the logic for updating an employee record
    """
    show_section_title('Update an Employee record')
    print('\n You chose to enter Update an Employee record.')
    press_enter_to_continue()


def Delete_an_Employee_record():
    """
        handles all the logic for deleting an employee record
    """
    show_section_title('Delete an Employee record')
    print('\n You chose to enter Delete an Employee record.')
    press_enter_to_continue()


# Call main()
if __name__ == "__main__":
    main(sys.argv)
