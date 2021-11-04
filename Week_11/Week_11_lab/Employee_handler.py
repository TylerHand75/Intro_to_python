#   FILE:   employee_handler.py
#   DATE:   2021-10-28
#   AUTHOR: Tyler Hand
#   DESCRIPTION:
"""
Functions that handle employee records.

MOD: 2021-10-14
MOD BY: tyler hand 
MOD discription: add functionality for the add_employee() function and the 
show_all_employee() function.

MOD: 2021-10-21
MOD BY: Tyler Hand 
MOD Discription: Added try except structures to handle possable exceptions 
    and changed add_employee() to only allow possitive integers fro id 

MOD: 2021-10-28
MOD BY: Tyler Hand 
MOD Discription: chaned to use lists as employee records. this requires moving
    the file reading and writing to thier own functions. we also add the 
    functionality for view and employee.

MOD: 2021-11-04
MOD BY: Tyler Hand 
MOD Discription: impiment the functionality for updating and deleting 
    employee records.this requires reading all the records as a list
    and then write a list to the file this overwrites the existing file. 
    to keep things simple selecting an employee record is done with the 
    employee id. also, the update funtionality will not allow the user to
    change the id. only non id-feilds. 

"""


import ui_helper

FILE_NAME ='Employee_data.csv'
"""
name of the file holding the employee records.
we put it in a constent because we will refer to it from several functions

the file will have the records fields each saperated by a comm. one per line
the fields are employee id, last name, first name, department, and salary 
"""
ID_IDX = 0 
"""index for id """
LNAME_IDX = 1 
"""index for last name"""
FNAME_IDX = 2
"""index for first name"""
DEPT_IDX =3
"""index for department"""
SALARY_IDX = 4
"""index for salary """


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
    id = ui_helper.get_user_possitive_integer("Employee ID: ")
    # get the last name 
    last_name = ui_helper.get_user_string("Last name: ")
    # get the first name 
    first_name = ui_helper.get_user_string("First name: ")
    # get the department
    dept = ui_helper.get_user_string("Department: ")
    # get the annual salary 
    salary = ui_helper.get_user_float("Annual salary: ")
    # build a record from the user input  
    record = [id, last_name, first_name, dept, salary]
    # open the file in appened mode and write the line
    try: 
        add_record_to_file(record)
        # let the user know we are done
        ui_helper.show_message("Employee records Saved. ")
    except Exception as err:
            ui_helper.show_message(str(err))
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
    try:
        record_list = get_all_records()
        if len(record_list) > 0:
            # loop through the employee records and display them 
            for record in record_list:
                id = record[ID_IDX]
                last_name = record[LNAME_IDX]
                first_name = record[FNAME_IDX]
                full_name = last_name + ', ' + first_name
                dept = record[DEPT_IDX]
                salary = record[SALARY_IDX]
                outputs = f'| {id:^10d} | {full_name:<30s} | {salary:>15.2f} |'\
                    f' {dept:<12s} |'
                ui_helper.show_message(outputs)
                ui_helper.show_bar()
            ui_helper.show_message("\nAll Employees are shown. ")
        else: 
            ui_helper.show_message("There are no employee records. ")
    except Exception as err:
        ui_helper.show_message(str(err))

    # tell the user to press enter 
    ui_helper. press_enter_to_continue()


def view_an_employees_records():
    """
        ask the user for an employee id. and search for that employee. 
        if found display details. if not found display a message stating so.
    """
    ui_helper.show_section_title('View an employees records')
    id = ui_helper.get_user_possitive_integer('Please enter the Employee ID: ')
    try:
        records = get_all_records()
        found = False
        for record in records:
            if record[ID_IDX] == id:
                found = True
                ui_helper.show_message('\nEmployee Data')
                ui_helper.show_message('ID: ' + str(id))
                ui_helper.show_message('Last Name: ' + record[LNAME_IDX])
                ui_helper.show_message('First Name: ' + record[FNAME_IDX])
                ui_helper.show_message('Department: ' + record[DEPT_IDX])
                salary_string = f'Salary: {record[SALARY_IDX]:.2f}'
                ui_helper.show_message(salary_string)
                break
        if not found: 
            message = f'\n There are no employees with ID {id}. '
            ui_helper.show_message(message)
    except Exception as err:
        ui_helper.show_message(str(err))
    ui_helper.press_enter_to_continue()


def Update_an_Employee_record():
    """
        ask the user for an employee ID. loop through the list of the employee
        until we find one with the matching ID. if found ask the user for the 
        values for the employee record, and save the records
        if not found, display a message saying so.
    """
    ui_helper.show_section_title('Update an Employee record')
    # Get the id 
    id = ui_helper.get_user_possitive_integer('Please enter Employee ID: ')
    try:
        records = get_all_records()
        if len(records) > 0 :
            found = False
            for record in records:
                if id == record[ID_IDX]:
                    found = True
                    # last name
                    prompt = f'Last Name or Blank to keep current ({record[LNAME_IDX]}): '
                    last_name = ui_helper.get_user_string(prompt)
                    if last_name.strip()== " ":
                        last_name = record[LNAME_IDX]
                    record[LNAME_IDX] = last_name
                    # first name
                    prompt = f'First Name or Blank to keep current ({record[FNAME_IDX]}): '
                    first_name = ui_helper.get_user_string(prompt)
                    if first_name.strip()== " ":
                        first_name = record[FNAME_IDX]
                    record[FNAME_IDX] = first_name
                    # department
                    prompt = f'Department or Blank to keep current ({record[DEPT_IDX]}): '
                    dept = ui_helper.get_user_string(prompt)
                    if dept.strip()== " ":
                        dept = record[DEPT_IDX]
                    record[DEPT_IDX] = dept
                    # salary 
                    prompt = f'Salary ({record[SALARY_IDX]}): '
                    salary = ui_helper.get_user_float(prompt)
                    record[SALARY_IDX] = salary
                    # save 
                    save_records(records)
                    break
            if not found:
                ui_helper.show_message(f'\nNo Employee found with ID {id}. ')
        else: 
            ui_helper.show_message("There are no employee records. ")
    except Exception as err:
        ui_helper.show_message(str(err))

    ui_helper. press_enter_to_continue()


def Delete_an_Employee_record():
    """
        ask teh user for the employee id of the employee record to delete
        loop through the list of employee, keeping any record that does not
        match the id givin. 
        if the id wa found, save the list of kept records to FILE_NAME

        if not found display message saying so

    """
    ui_helper.show_section_title('Delete an Employee record')
    id = ui_helper.get_user_possitive_integer('Please enter the Employee ID: ')
    try: 
        records = get_all_records()
        if len(records) > 0 :
            found = False
            keep = []
            for record in records:
                if id != record[ID_IDX]:
                    keep.append(record)
                else: 
                    found = True
            if not found:
                ui_helper.show_message(f'\nNo Employee with {id}. ')
            else: 
                save_records(keep)
                ui_helper.show_message(f'\nDeleted Employee with {id}. ')
        else: 
            ui_helper.show_message('There are no employee records. ')
    except Exception as err:
        ui_helper.show_message(str(err))

    ui_helper.press_enter_to_continue()


# #############################################################################
# File funtions
# these are the functions for working with the file
# #############################################################################


def build_csv_line(record):
    """takes and employee record as a list and converts it into a 
       csv formatted string. 

       Input:  
            record list and employee records
        returns: 
            string the record in csv format
    """
    line = str(record[ID_IDX]) + ',' + record[LNAME_IDX] + ','\
        + record[FNAME_IDX] + ',' + record[DEPT_IDX] + ',' \
            + str(record[SALARY_IDX]) + '\n'
    return line

def add_record_to_file(record):
    """
    takes a record as a list, and appends the record to the end of FILE_NAME.
    this does not handle any exeptions. the excptions are allowed to go back
     to the calling finctions. this is called "bubbling up". 
     it is assumed that the calling funtion has a better idea of how 
     to handle any issues. 

     Inputs: 
        record a list represention an employee record. 
    """
    line = build_csv_line(record)
    with open(FILE_NAME, 'a') as out_file:
        out_file.write(line)

def get_all_records():
    """
    attempts to open FILE_NAME and read all the records. storing each as a 
    list, and placing all of them into a larger list 

    if there are no records in the CSV file, the empty list is returened 
    
    file has no excpetions

    returns:
        list a list with all the employee records.
    """

    records = []
    with open(FILE_NAME, 'r') as in_file:
        for line in in_file:
            fields = line.split(',')
            id = int(fields[ID_IDX])
            salrary = float(fields[SALARY_IDX])
            record = [id,fields[LNAME_IDX], fields[FNAME_IDX], \
                fields[DEPT_IDX], salrary]
            records.append(record)
    return records


def save_records(records):
    """
        loops through the supplied record and write them to FILE_NAME as a 
        csv file. this overwrites any data in the file. 

        Inputs:
            records a list of employee records, which are also lists.

    """
    with open(FILE_NAME, 'w') as out_file:
        for record in records: 
            line = build_csv_line(record)
            out_file.write(line)









