#   FILE:   user_int_example.py
#   DATE:   2021-10-19
#   AUTHOR: Tyler Hand
#   DESCRIPTION:
"""
using try-except to get an int from the user
"""

# We want to ask teh user for an int, but they may enter something else.
# ValueError
needed = True
while needed:
    try:
        value = int(input('Enter a Whole number: '))
        needed = False 
    except ValueError:
        print('This is not a whole number. please try agian. ')

print(f'You entered {value}')
