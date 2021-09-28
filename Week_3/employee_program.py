#   FILE:   employee_program.py
#   DATE:   2021-09-09
#   AUTHOR: Tyler Hand
#   DESCRIPTION:
"""
this is the starting program for the employee program example. 
the employee program example will grow and change as a new concepts are added throughout the semester.

"""

# inputs
# employee_id int entered by user
# last_name string ebu
# first_name string ebu
# depaertment string ebu
# salary float ebu
# process
# Show the program title
# Get the values from the user
# build the full name based on the last_name and first_name
# disply the outputs 
# tell the user the program is done
# outputs 
# a header row showing the names of the data columns
# a single formatted row consisting of the following values, field widths, and field justifications: 
# 1) department, 15  characters wide, left justified
# 2) employee_id, 10 characters wide, centered 
# 3) full_name, 50 characters wide, left justified
# 4) salary, 15 characters wide, right jsutified

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

    program_title = "*** Employee Program ***"
    print(f'\n{program_title:^{CONSOLE_WIDTH}}')

    # Define the prompt strings

    employee_id_prompt = "Please enter the employee Id: "
    last_name_prompt = "Please enter the employee last name: "
    first_name_prompt = "Please enter the employee first name: "
    department_prompt = "Please enter the department name: "
    salary_prompt = "Please enter the employee annual salary: "

    #strings for final output

    table_name = "Employee Data"
    bar = "-" * CONSOLE_WIDTH #horizontal line 
    dep_header = "Department"
    id_header = "Id"
    emp_name_header = "Employee Name"
    salary_header = "Salary"
    program_complete = "Program Complete"

    # Get the inputs

    employee_id = int(input(employee_id_prompt))
    last_name = input(last_name_prompt)
    first_name = input(first_name_prompt)
    Departmemt= input(department_prompt)
    salary = float(input(salary_prompt))

    # Perform Processing

    full_name = last_name + ", " + first_name

    # Display the outputs 

    print(f"\n{table_name: ^{CONSOLE_WIDTH}}")
    print(bar)
    print(f'| {dep_header:^12s} | {id_header:^10s} | {emp_name_header:^30s} | {salary_header:^15s} |')
    print(bar)

    #print the data row 

    print(f'| {Departmemt:<12s} | {employee_id:^10d} | {full_name:<30s} | {salary:>15.2f} |')
    print(bar)

    # Let the use know the program is done
    
    print(f"\n{program_complete}\n")
   

# Call main()
if __name__ == "__main__":
    main(sys.argv)
