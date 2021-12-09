#   FILE:   ui_helper.py
#   DATE:   2021-10-07
#   AUTHOR: Class
#   DESCRIPTION:
""" 
    Functions for interacting with the user.

MOD DATE:   2021-10-14
MOD BY:     Bob Trapp
MOD DESCRIPTION: Added function get_user_int(), get_user_float(), show_bar().
    Added constant CONSOLE_WIDTH.

MOD DATE:   2021-10-21
MOD BY:     Bob Trapp
MOD DESCRIPTION: Added try-except structures to handle Exceptions and added
    the function get_user_positive_int().





"""

CONSOLE_WIDTH = 80
""" 
A default console width to use.
"""

# #############################################################################
# Functions for general user interaction
#   These functions separate the View logic from the Control and Model 
#   logic.
# #############################################################################
def show_program_title(title, width):
    """ 
        Displays the program title in a consistent manner.
    
    INPUTS:
        title String with the title of the program
        width The width of the screen, used for centering

    """ 
    new_title = '*** ' + title.upper() + ' ***'
    print(f'\n{new_title:^{width}}')


def show_section_title(title):
    """ 
        Displays the section title in a consistent format.
    
    INPUTS:
        title String containing the title text of the section
    """
    print(f'\n\t-- {title} --')

def press_enter_key_to_continue():
    """
        Display a message telling the user to press the Enter key to 
        contiunue.  Wait until they do.  Ignore anything else they enter.

    """
    input('\nPress the Enter key to continue... ')

def show_message(message):
    """ 
    Displays a message in a consistent format.

    INPUTS: 
        message string A string containing the message text
    """
    print(message)

def get_user_int(prompt):
    """
    Prompt the user to enter an int and return that int value.
    If the users enters something that is not an int, then the function
    displays an error message and tells them to try again.

    INPUTS:
        prompt string A string with instructions for the user

    RETURNS:
        int The int value entered by the user

    """
    value = 0
    needed = True
    error_message = 'That is not a valid integer.  Please try gain.'
    while needed:
        user_value = input(prompt + ' ')
        try:
            value = int(user_value)
            needed = False
        except:
            show_message(error_message)
    return value

def get_user_float(prompt):
    """ 
    Prompt the user to enter an float and return that float value.
    If the users enters something that is not an float, then the function
    displays an error message and tells them to try again.

    INPUTS:
        prompt string A string with instructions for the user

    RETURNS:
        float The float value entered by the user

    """ 
    value = 0
    needed = True
    error_message = 'That is not a valid number.  Please try gain.'
    while needed:
        user_value = input(prompt + ' ')
        try:
            value = float(user_value)
            needed = False
        except:
            show_message(error_message)
    return value

def get_user_positive_integer(prompt):
    """ 
    Prompt the user to enter a positive integer and return that integer.
    If they enter anything that is not a positive integer, display an 
    error message and tell them to try again.

    INPUTS:
        prompt string Instructions for the user

    RETURNS:
        int A positive integer

    """ 
    value = 0
    needed = True
    error_message = 'That is not a positive number.  Please try again.'
    while needed:
        value = get_user_int(prompt)
        if value >= 0:
            needed = False
        else:
            show_message(error_message)
    return value




def show_bar():
    """ 
    Draw a horizontal line made up of '*' characters across the screen.
    """ 
    bar = '*' * CONSOLE_WIDTH
    show_message(bar)



# #############################################################################
# Menu Functions
# #############################################################################
def get_user_choice():
    """ 
        Display the menu and ask the user to choose something.

    RETURNS:
        string The user's choice
    """ 
    menu_title = 'Main Menu'
    prompt =  "Your choice: "
    options = ['1) Add an Employee','2) Show All Employees','3) View an Employee'
        ,'4) Update an Employee','5) Delete an Employee','Q) Quit']
    show_menu(menu_title, options)
    return get_user_string(prompt)

def show_menu(menu_title, options):
    """ 
        Display a menu in a structured format. 
    
    INPUTS: 
        menu_title A string with the title of the menu
        options A list containing strings for the menu options
    """ 
    print(f'\n\n\t-- {menu_title} --')
    for option in options:
        print(f'\t{option}')

def get_user_string(prompt):
    """ 
        Prompts the user enter a string and retuns the string.
    """
    return input(prompt + ' ') 


def confirm_quit():
    """ 
        Display a message stating that the user has chosen to quit.
        Ask the user to confirm by entering Y or N.  If the user enters
        Y or y then return True, otherwise False.
    """ 
    print("You chose to Quit.")
    choice = get_user_string("Confirm (Y/N) ")
    return choice == 'Y' or choice == 'y'



