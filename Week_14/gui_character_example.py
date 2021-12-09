#   FILE:   gui_character_example.py
#   DATE:   2021-12-02
#   AUTHOR: Class
#   DESCRIPTION:
"""
An attempt to display non-English characters.

"""
import tkinter
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
    main_window = tkinter.Tk()

    # Add a label
    my_label = main_window.label = tkinter.Label(main_window, text='بدء البرنامج')
    my_label.pack()

    # Enter the window main loop
    tkinter.mainloop()

# Call main()
if __name__ == "__main__":
    main(sys.argv)


