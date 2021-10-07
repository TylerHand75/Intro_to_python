#   FILE:   employee_handler.py
#   DATE:   2021-10-07
#   AUTHOR: Tyler Hand
#   DESCRIPTION:
"""
Functions that handle employee records
"""
import ui_helper
# #############################################################################
# employee handiling functions
# these are the functions for working with employee records
# #############################################################################


def add_employee():
    """
        handles all the logic for adding an employee record
    """
    ui_helper.show_section_title('Add an employee')
    print('\n You chose to enter an new employee record.')
    ui_helper.press_enter_to_continue()


def show_all_employees():
    """
        handles all the logic for showing all employees
    """
    ui_helper.show_section_title('Show all employees')
    print('\n You chose to enter Show all employees.')
    ui_helper. press_enter_to_continue()


def view_employees_records():
    """
        handles all the logic for viewing an employee record
    """
    ui_helper.show_section_title('View employees records')
    print('\n You chose to enter View employees records.')
    ui_helper.press_enter_to_continue()


def Update_an_Employee_record():
    """
        handles all the logic for updating an employee record
    """
    ui_helper.show_section_title('Update an Employee record')
    print('\n You chose to enter Update an Employee record.')
    ui_helper. press_enter_to_continue()


def Delete_an_Employee_record():
    """
        handles all the logic for deleting an employee record
    """
    ui_helper.show_section_title('Delete an Employee record')
    print('\n You chose to enter Delete an Employee record.')
    ui_helper.press_enter_to_continue()
