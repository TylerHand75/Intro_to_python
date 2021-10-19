#   FILE:   number_adder.py
#   DATE:   2021-10-19
#   AUTHOR: Tyler Hand
#   DESCRIPTION:
"""
open a text file contaning numebrs, read the numbers, addd them, and display 
the sum
"""

FILE_NAME = 'numbers.txt'

def main():
    """
    manin logic goes here
    """
    accumulator = 0 
    try: 
        in_file = open(FILE_NAME, 'r')
        for line in in_file:
            accumulator += int(line)
        in_file.close()
        print(f'Total: {accumulator}')
    except ValueError as Err:
        print('Ooops', Err)
    except FileNotFoundError as fnf:
        print(fnf)
    except Exception as ex:
        print(ex)
    finally:
        in_file.close()


main()