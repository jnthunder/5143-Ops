#!/usr/local/bin/python3

""" Main funtion: for the implementation of the Less a File command """

##################################### __less__ ###################################
##################################################################################

import os
import curses
import keyboard
from Getch import Getch

def less(**kwargs):
    L = 0
    File = ""
    FILE = kwargs.get('params') # Use 'file' instead of 'params' to get the file name
    G = Getch()                 # Sets the getch function to a variable
    C = curses.initscr()        # sets curses.initscr to a variable
    curses.curs_set(0)          # Hides the cursor while going through the pages

    for l in FILE:
        File += l

    try:
        with open(File, 'r') as file:   # Opens and reads file
            lines = file.readlines()

    except FileNotFoundError:           # If the file name is either incorrect or not found
        print("File not found.")
        return

    page_size = C.getmaxyx()[0]         # Number of lines that fit on one page
    current_page = 0

    while True:
        height, width = C.getmaxyx()    # determines how many lines are required

        C.clear()

        start_line = current_page * page_size   # uses the pg size for each page by determining the start
        end_line = start_line + height          # uses the pg size for each page by determining the end

        for i in range(start_line, min(end_line, len(lines))):  # for loop for determining the above
            try:
                C.addstr(i - start_line, 0, lines[i])
            except curses.error:
                pass

        C.refresh()

        ch = G()
        print(ch)
        if ch == 'q':                           # when getch sees the q button is pressed it ends and closes the function
            curses.curs_set(1)                  # cursor is reset/ready for next command
            break
        elif ch == 'n':                         # when n is pressed: the next page is retrieved
            current_page = min(current_page + 1, len(lines) // page_size)
        elif ch == 'm':                         # when n is pressed: the previous page is retrieved 
            current_page = max(0, current_page - 1)
