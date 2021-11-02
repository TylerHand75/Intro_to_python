#   FILE:   Rainfall_Staistics.py
#   DATE:   2021-10-30
#   AUTHOR: Tyler Hand
#   DESCRIPTION:
"""
Description of file goes here.

"""

import sys

# A constant for the number of characters across the console
CONSOLE_WIDTH = 80

def rainfall_generator():
    rainfall_list = []
    for i in range(12):
        monthly_rain = float(input("Enter rain for month: "))
        rainfall_list.append(monthly_rain)
    return rainfall_list


def rainfall_total(a):
    total = 0
    for monthly_rain in a:
        total += monthly_rain
    return total

def main(argv):
    """
    Description of main() goes here.

    INPUTS:
        argv A list of strings representing the command line arguments

    RETURNS:
        None
    """
    # Show the program title
    program_title = "*** Rainfall Staistics ***"
    print(f'\n{program_title:^{CONSOLE_WIDTH}}')
    # Get the inputs
    
    # Perform Processing
    rainfall = rainfall_generator()
    total_rainfall = rainfall_total(rainfall)
    avg_monthly_rain = total_rainfall/12
    lowest_rain_month = rainfall.index(min(rainfall))
    highest_rain_month = rainfall.index(max(rainfall))
    print("Total Rainfall for the Year:",total_rainfall)
    print("Average monthly rain:",avg_monthly_rain)
    print("The month with the lowest rain is:",lowest_rain_month+1)
    print("The month with the highest rain is:",highest_rain_month+1)
    
    # Display the outputs
    
   
    # Let the use know the program is done
    print("\nProgram complete.\n")
   

# Call main()
if __name__ == "__main__":
    main(sys.argv)


