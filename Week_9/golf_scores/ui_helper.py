#   FILE:   ui_helper.py
#   DATE:   2021-10-24
#   AUTHOR: Tyler Hand
#   DESCRIPTION:
"""
this is the ui_helper for the golf scores program

"""


CONSOLE_WIDTH = 80
"""
default console width 
"""


def show_program_title(title, WIDTH):
    """Displays the program title in a consitent manor 

    inputs: title sting with the title of the program 
    width the width of the screen, used for centering.
    """
    new_title = '*** ' + title.upper() + ' ***'
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

def show_message(message):
    """
    displays a message in a consistant format.
    input: message a string 
    """
    print(message)

def get_user_int(prompt):
    """
    prompt the user to enter the int and return that int value. 
        if the user enters something that is not an int then the function 
        displays an error message and tells them to try again.

    Inputs:
        prompt string a string with instructions for the user     
    Returns:
        int the int value entered by the user. 
    """
    value = 0 
    needed = True
    error_message = "That is not a valid Integer. Please try again. "
    while needed:
        user_value =  input(prompt + " ")
        try: 
            value = int(user_value)
            needed = False
        except:
            show_message(error_message)
    return value

def get_user_float(prompt):
    """
    prompt the user to enter the float and return that float value. 

    Inputs:
        prompt string a string with instructions for the user     
    Returns:
        float the float value entered by the user.
    """
    value = 0 
    needed = True
    error_message = "That is not a valid number. Please try again. "
    while needed:
        user_value =  input(prompt + " ")
        try: 
            value = float(user_value)
            needed = False
        except:
            show_message(error_message)
    return value

def get_user_possitive_integer(prompt):
    """
    propmt the user to enter a passitive integer and return that integer 
    if they enter anything that is nit possitive, diplay an error message 
    and tell them to try again

    INPUTS: 
        prompt string instructions for the user
    RETURNS:
        int a possitive integer
    """
    value = 0 
    needed = True
    error_message = 'That is not a possitive number. Please try again. '
    while needed:
        value = get_user_int(prompt)
        if value >= 0:
            needed = False
        else: 
            show_message(error_message)
    return value


def show_bar():
    """
    draw a horizontal line made of '*' chartictars all the way across.
    """
    bar = '*' * CONSOLE_WIDTH
    show_message(bar)


def get_user_choice():
    """
        display the menu and ask the user to do something 
       Returns:
            string user's choice
    """
    menu_title = 'Main Menu'
    prompt = "Your choice: "
    options = ['1) Add a Player ', '2) show all Player Scores ',
               '3) Quit ']
    show_menu(menu_title, options)
    return get_user_string(prompt)


def show_menu(menu_title, options):
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
    return input(prompt + " ")


def confirm_quit():
    """
        displpay a message stating the user has chosen to Quit
        ask the user to confirm by entering Y or N. if the user enters
        Y or y the return True
    """
    print('You Chose to Quit')
    choice = get_user_string('Confirm (Y/N)')
    return choice == 'Y' or choice == 'y'