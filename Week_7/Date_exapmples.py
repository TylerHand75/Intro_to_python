#   FILE:   Example_week_7.py
#   DATE:   2021-10-5
#   AUTHOR: Tyler Hand
#   DESCRIPTION:
"""
Demonstating using moduals. using dates in python.
"""
import datetime
import sys
from time import time

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
    program_title = "*** Date examples ***"
    print(f'\n{program_title:^{CONSOLE_WIDTH}}')
   # get todays date and time

    today = datetime.datetime.now()
    print("Current date and time: ", today)

    current_date = datetime.date.today()
    print("Current date:" , current_date)
    # Date parts
    print("Current Year:", today.year)
    print("Current Month:", today.month)
    print("Current Day :", today.day)
    print("Current Hour:", today.hour)
    print("Current Minute:", today.minute)
    # next week
    one_week=datetime.timedelta(days=7)
    print("Next week:", ( today + one_week))
    print("Last week:", ( today - one_week))

    # formated date
    print("Formated Date:", today.strftime("%A %B %d, %Y"))
   
    # Let the use know the program is done
    print("\nProgram complete.\n")
   

# Call main()
if __name__ == "__main__":
    main(sys.argv)


