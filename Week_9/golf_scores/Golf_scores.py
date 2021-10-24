#   FILE:   employee_program.py
#   DATE:   2021-10-24
#   AUTHOR: Tyler Hand 
#   DESCRIPTION:
"""
this is menu program to get the inputs of the players name and score. then to 
save them to a file and then to display them

"""
import Player_handler
import ui_helper
import sys

# A constant for the number of characters across the console
CONSOLE_WIDTH = 80
VERSION = "1.0.0"


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
    print(argv)
    if len(argv) == 1:
        do_program_logic()   
    elif len(argv) == 2:
        if argv [1] == '-?' or argv[1]== '-h' or argv[1] =='--help':
            show_help()
        elif argv[1] == '-v'or argv[1] == '--version':
            show_version()
        else:
            show_error ('invalid command line argument: ' + argv[1])
    else: show_error('invalid count of comand line arguments: ') + str(argv)
    

def show_version():
    """
    display the current version of the program
    """
    ui_helper.show_message(f'\n Employee program {VERSION}')
    sys.exit(0)

def show_help():
    """
    display the usage information for this program 
    """
    ui_helper.show_message("\nUsage: ")
    ui_helper.show_message("Python employee_program.py")
    ui_helper.show_message("Python employee_program.py [ -? | -h | --help]")
    ui_helper.show_message("Python employee_program.py[ -v | --version]\n")

def show_error(message):
    """
    display the error message, display the help, then exit with a none 0 value
    inputs : message string the text error message.
    """
    ui_helper.show_message(f"\nERROR:{message}")
    show_help()
    sys.exit(1)
   
# #############################################################################
# functions to respond to the comand line elements arguments
# #############################################################################


def do_program_logic():
    """
    this is the primanry programing logic implmenting the menu.
    it repersents the primarty starting point for the comon use of this program
    """
    program_title = 'Employee Program'
    ui_helper.show_program_title(program_title, CONSOLE_WIDTH)
    done = False
    invalid_option_message = "Your choice was not recognized. Try again."
    while not done:
        user_choice = ui_helper.get_user_choice()
        if user_choice == '1':
            Player_handler.add_player()
        elif user_choice == '2':
             Player_handler.show_all_players()
        elif user_choice == 'Q' or user_choice == 'q':
            done = ui_helper.confirm_quit()
        else:
            ui_helper.show_message(invalid_option_message)


         # Let the use know the program is done
        ui_helper.show_message("\nProgram complete.\n")


# Call main()
if __name__ == "__main__":
    main(sys.argv)
