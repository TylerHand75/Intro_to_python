#   FILE:   Calories_from_fat_to_carbs.py
#   DATE:   2021_10_10
#   AUTHOR: Tyler Hand
#   DESCRIPTION:
"""
This is a program to calculate the ammount of calories from fat and carbohydrates. 

"""

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
    program_title = "*** TITLE ***"
    print(f'\n{program_title:^{CONSOLE_WIDTH}}')
    
    fat_grams = float(input("Enter the number of fat grams consumed: "))
    fat_calories(fat_grams)
    carb_grams = float(input("Enter the number of carbohydrate grams consumed: "))
    carb_calories(carb_grams)

def fat_calories(fat_grams):
    calories_from_fat = fat_grams * 9
    print ("The calories from fat are", (calories_from_fat))

def carb_calories(carb_grams):
    calories_from_carbs = carb_grams * 4
    print ("The calories from carbohydrates are", (calories_from_carbs))


    print("\nProgram complete.\n")
   

# Call main()
if __name__ == "__main__":
    main(sys.argv)


