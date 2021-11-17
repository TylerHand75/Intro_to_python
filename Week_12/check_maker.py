#   FILE:   code_template.py
#   DATE:   <date here in ISO-8601 format>
#   AUTHOR: <student name here>
#   DESCRIPTION:
"""
Description of file goes here.

"""
import Employee_handler
import datetime
import math 
import sys

# A constant for the number of characters across the console
CONSOLE_WIDTH = 80

LAST_CHECK_NUMBER = 1024
""" A pretend last check number to use a starting point """

def main(argv):
    """
    Description of main() goes here.

    INPUTS:
        argv A list of strings representing the command line arguments

    RETURNS:
        None
    """
    # Show the program title
    program_title = "*** Check Maker ***"
    print(f'\n{program_title:^{CONSOLE_WIDTH}}')
    # Get the inputs
    records = employee_handler.get_all_records()
    check_date = datetime.date.today()
    check_number = LAST_CHECK_NUMBER
    with open("check_template.txt", "r") as in_file:
        template = in_file.read()
    # Perform Processing
    for record in records:
        full_name = record[2] + ' ' + record[1]
        amount = (record[4] / 24) * .8 # numeric value
        pay_amount = f'{amount:.2f}' # string formatted for display
        text_amount = build_text_amount(amount)
        check_number = check_number + 1
        check = template 
        check = check.replace('<date>', str(check_date))
        check = check.replace('<check_number>', str(check_number))
        check = check.replace("<name>", full_name)
        check = check.replace("<amount>", pay_amount)
        check = check.replace("<text_amount>", text_amount)
        print(check)
    # Display the outputs
    # Let the use know the program is done
    print("\nProgram complete.\n")

def build_text_amount(amount):
    """     
    Builds a string representing the dollar amount of the check.

    INPUTS:
        amount The dollar amount to convert
    
    RETURNS:
        string A string containing the text version of the amount.
    """
    text = ''
    # Handle the thousands
    thousands = int(amount // 1000)
    if thousands > 0:
        text += value_to_text(thousands) + " Thousand "
    # Handle the hundreds
    hundreds = (amount % 1000) // 100
    if hundreds > 0:
        text += value_to_text(hundreds) + " Hundred "
    # Handle the tens
    tens = (amount % 100) // 10
    ones = int(amount % 10)
    if tens > 0 or ones > 0:
        text += tens_value_to_text(tens, ones) + " "
    # Handle the ones
    # Handle the cents
    frac, whole = math.modf(amount)
    
    return text  

def value_to_text(value):
    """ """
    result = ""
    if value == 9:
        result = "Nine"
    elif value == 8:
        result = "Eight"
    elif value == 7:
        result = "Seven"
    elif value == 6:
        result = "Six"
    elif value == 5:
        result = "Five"
    elif value == 4:
        result = "Four"
    elif value == 3:
        result = "Three"
    elif value == 2:
        result = "Two"
    else:
        result = "One"
    return result


def tens_value_to_text(value, ones):
    """ """
    result = ""
    if value == 9:
        result = "Ninety " + value_to_text(ones)
    elif value == 8:
        result = "Eighty " + value_to_text(ones)
    elif value == 7:
        result = "Seventy " + value_to_text(ones)
    elif value == 6:
        result = "Sixty " + value_to_text(ones)
    elif value == 5:
        result = "Fifty " + value_to_text(ones)
    elif value == 4:
        result = "Forty " + value_to_text(ones)
    elif value == 3:
        result = "Thirty " + value_to_text(ones)
    elif value == 2:
        result = "Twenty " + value_to_text(ones)
    else:
        if ones == 9:
            result = 'Nineteen'
        elif ones == 8:
            result = 'Eighteen'
        elif ones == 7:
            result = 'Seventeen'
        elif ones == 6:
            result = 'Sixteen'
        elif ones == 5:
            result = 'Fifteen'
        elif ones == 4:
            result = 'Fourteen'
        elif ones == 3:
            result = 'Thirteen'
        elif ones == 2:
            result = 'Twelve'
        elif ones == 1:
            result = 'Eleven'
        elif ones == 0:
            result = 'Ten'

    return result
    
    # Let the use know the program is done
    print("\nProgram complete.\n")
   

# Call main()
if __name__ == "__main__":
    main(sys.argv)


