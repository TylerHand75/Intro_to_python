#   FILE:   lab_14.py
#   DATE:   2021-12-02
#   AUTHOR: Class
#   DESCRIPTION:
"""
The program uses a dictionary to hold needed output.
There are different files for different human languages.
The language must be specified on the command line or the program 
defaults to English.

Note that the terminal may display some characters correctly.

The two-letter languates codeed are based on ISO-639-1 international
standard:
https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes

"""

import ui_helper
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
    # Get the language 
    language = figure_language(argv)
    out_dict = get_strings(language)
    # Show the program title
    program_title = "*** Lab 14 ***" # usually will not translate the name
    print(f'\n{program_title:^{CONSOLE_WIDTH}}')
    ui_helper.show_message(out_dict['program_starting'])
    # Get the inputs
    # Perform Processing
    # Display the outputs
    # Let the use know the program is done
    ui_helper.show_message(out_dict['program_complete'])



def figure_language(sys_argv):
    """ 
    Check that the length of sys_argv is 2, then get the second element.  
    If the length is not 2, use English as the language.

    INPUTS:
        sys_argv A list of command line arguments

    RETURNS:
        string The two-letter language code
    """
    lang = 'en' # English as default
    if len(sys_argv) == 2:
        lang = sys_argv[1].strip().lower()
    return lang

def get_strings(language):
    """ 
    Build a title for the language file and then attempt to 
    read that file.

    INPUTS:
        language The two-letter language code 
    
    RETURNS:
        dictionary A dictionary with the available output text
    """ 
    file_name = 'example_' + language + '.properties'
    print(file_name)
    text = {}
    with open(file_name, 'r') as in_file:
        for line in in_file:
            line = line.strip()
            if len(line) > 0 and not line.startswith('#'):
                fields = line.split('=')
                key = fields[0].strip()
                value = fields[1].strip()
                text[key] = value
    return text




# Call main()
if __name__ == "__main__":
    main(sys.argv)


