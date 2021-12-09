#   FILE:   Word_Frequency.py
#   DATE:   2021-11-30
#   AUTHOR: Example
#   DESCRIPTION:
"""
Programming Exercise 5 on page 486 of the Gaddis text.

"""

import sys

# A constant for the number of characters across the console
CONSOLE_WIDTH = 80

FILE_NAME = 'Dialogues_of_the_Dead_by_Baron_George_Lyttelton_Lyttelton_and_Mrs_Montagu_Two_Paragraphs.txt'
""" A constant for the name of the file. """

def main(argv):
    """
    Description of main() goes here.

    INPUTS:
        argv A list of strings representing the command line arguments

    RETURNS:
        None
    """
    if len(argv) != 3:
        print("Wrong command line arguments.")
        print('python Word_Frequency.py <source file> <output file>')
        exit(1)
    input_file_name = argv[1]
    output_file_name = argv[2]
    # Show the program title
    #program_title = "*** Word Frequency ***"
    #print(f'\n{program_title:^{CONSOLE_WIDTH}}')
    try:
        # Get the inputs
        text = get_file_text(input_file_name)
        # Perform Processing
        word_dict = process_text(text)
        write_frequencies(word_dict, output_file_name)
    except Exception as err:
        print(err)
    # Let the use know the program is done
    #print("\nProgram complete.\n")


def get_file_text(file_name):
    """ 
    Reads text from the specified file and returns it.

    INPUTS:
        file_name The name of the file to read.

    RETURNS:
        string The contents of the file.
    """
    with open(file_name, 'r') as in_file:
        text = in_file.read()
    return text

def process_text(text):
    """ 
    Build a dictionary with the word frequencies from the supplied text.

    INPUTS:
        text The text to process

    RETURNS:
        dictionary A dictionary with the word frequencies
    """ 
    word_dict = {}
    words = text.split()
    for word in words:
        if word not in word_dict:
            word_dict[word] = 0
        word_dict[word] += 1
    return word_dict

def write_frequencies(word_dict, out_file_name):
    """ 
    Writes the word frquencies to a text file.

    INPUTS:
        word_dict A dictionary with the word frequencied
        out_file_name A string with the name of the output file
    """
    with open(out_file_name, 'w') as out_file:
        for k, v in word_dict.items():
            line = f'{k}|{str(v)}\n'
            out_file.write(line)


# Call main()
if __name__ == "__main__":
    main(sys.argv)


