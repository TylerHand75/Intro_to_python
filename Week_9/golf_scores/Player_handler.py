#   FILE:   employee_handler.py
#   DATE:   2021-10-24
#   AUTHOR: Tyler Hand
#   DESCRIPTION:
"""
this it is the player_handler for the golf_scores program

"""
import ui_helper

FILE_NAME ='golf_scores.csv'


def add_player():
    """
    handles all the file adding functions 
    """
    ui_helper.show_section_title('Add a player')
    # get the employee id 
    # get the last name 
    last_name = ui_helper.get_user_string("Last name: ")
    # get the first name 
    first_name = ui_helper.get_user_string("First name: ")
    # get the department
    score = ui_helper.get_user_string("Score: ")
    # get the annual salary 
    # format the line for output 
    line = last_name + "," + first_name + "," + str(score) + "\n"

    # open the file in appened mode and write the line
    try: 
        out_file = open(FILE_NAME, 'a')
        out_file.write(line)
    except Exception as err:
            ui_helper.show_message(str(err))
    finally: 
        try: 
            out_file.close()
        except:
            pass
    # close the file
    out_file.close()
    # let the user know we are done
    ui_helper.show_message("Employee records Saved. ")
    # tell the user to press the Enter key 
    ui_helper.press_enter_to_continue()


def show_all_players():
    """
    handles all the player logic
    """
    ui_helper.show_section_title('Show all players')
    # open the file in read mode
    try:
        in_file = open(FILE_NAME, "r")
        # Draw the table header
        score_header = 'SCORE'
        player_name_header = 'PLAYERS NAME'
        header = f'| {player_name_header:^29s} '\
            f' | {score_header:^30s} |'
        ui_helper.show_message('\n\n')
        ui_helper.show_bar()
        ui_helper.show_message(header)
        ui_helper.show_bar()
        # loop through the employee records and display them 
        for line in in_file:
            fields = line.split(',')
            last_name = fields[0]
            first_name = fields[1]
            full_name = last_name + ', ' + first_name
            scores = fields[2]
            
            outputs = f'| {full_name:<30s} | {scores:>15s} '
            ui_helper.show_message(outputs)
            ui_helper.show_bar()
    except Exception as err:
        ui_helper.show_message(str(err))
    finally: 
        try: 
            in_file.close()
        except:
            pass
    # tell teh user we are done 
    ui_helper.show_message("\nAll player are shown. ")
    # tell the user to press enter 
    

    ui_helper. press_enter_to_continue()


def view_player_scores():
    """
    handles the display of the players scores
    
    """
    ui_helper.show_section_title('View Players scores')
    print('\n You chose to enter View all players scores.')
    ui_helper.press_enter_to_continue()



