#   FILE:   employee_handler.py
#   DATE:   2021-10-07
#   AUTHOR: Tyler Hand
#   DESCRIPTION:
"""
Functions that handle employee records.

MOD: 2021-10-14
MOD: tyler hand 
MOD discription: add functionality for the add_employee() function and the 
show_all_employee() function.

"""
import ui_helper

FILE_NAME ='Employee_data.csv'
"""
name of the file holding the employee records.
we put it in a constent because we will refer to it from several functions

the file will have the records fields each saperated by a comm. one per line
the fields are employee id, last name, first name, department, and salary 
"""


# #############################################################################
# employee handiling functions
# these are the functions for working with employee records
# #############################################################################


def add_employee():
    """
        handles all the logic for adding an employee record

        this function ask the user for the employee data. then, it  apppends
        the employee data to the file named with FILE_NAME

    """
    ui_helper.show_section_title('Add an employee')
    # get the employee id 
    id = ui_helper.get_user_int("Employee ID: ")
    # get the last name 
    last_name = ui_helper.get_user_string("Last name: ")
    # get the first name 
    first_name = ui_helper.get_user_string("First name: ")
    # get the department
    dept = ui_helper.get_user_string("Department: ")
    # get the annual salary 
    salary = ui_helper.get_user_float("Annual salary: ")
    # format the line for output 
    line = str(id) + "," + last_name + "," + first_name + "," + dept + "," \
         + str(salary) +"\n"
    # open the file in appened mode and write the line
    out_file = open(FILE_NAME,"a")
    out_file.write(line) 
    # close the file
    out_file.close()
    # let the user know we are done
    ui_helper.show_message("Employee records Saved. ")
    # tell the user to press the Enter key 
    ui_helper.press_enter_to_continue()


def show_all_employees():
    """
        handles all the logic for showing all employees
        opens the file designated by FILE_NAME and reads and prints the 
        employee record
    """
    ui_helper.show_section_title('Show all employees')
    # open the file in read mode
    in_file = open(FILE_NAME, "r")
    # Draw the table header
    dept_header = 'DEPARTMENT'
    id_header = 'ID'
    emp_name_header = 'EMPLOYEE NAME'
    salary_header = 'SALARY'
    header = f'| {id_header:^10s} | {emp_name_header:^30s} '\
        f'| {salary_header:^15s} | {dept_header:^12s} |'
    ui_helper.show_message('\n\n')
    ui_helper.show_bar()
    ui_helper.show_message(header)
    ui_helper.show_bar()
    # loop through the employee records and display them 
    for line in in_file:
        fields = line.split(',')
        id = int(fields[0])
        last_name = fields[1]
        first_name = fields[2]
        full_name = last_name + ', ' + first_name
        dept = fields[3]
        salary = float(fields[4])
        outputs = f'| {id:^10d} | {full_name:<30s} | {salary:>15.2f} |'\
            f' {dept:<12s} |'
        ui_helper.show_message(outputs)
        ui_helper.show_bar()
    # close the file 
    in_file.close()
    # tell teh user we are done 
    ui_helper.show_message("\nAll Employees are shown. ")
    # tell the user to press enter 
    

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
