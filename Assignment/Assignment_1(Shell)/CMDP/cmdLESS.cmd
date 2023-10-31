#!/usr/local/bin/python3

""" Main funtion: for the implementation of the Less a File command """

##################################### __less__ ###################################
##################################################################################

import os
import curses
import keyboard
from Getch import Getch

def less(**kwargs):
    L = 0                               # Initialize L to 0
    File = ""                           #Initialize File to a string
    FILE = kwargs.get('params')         # Use 'file' instead of 'params' to get the file name
    G = Getch()
    C = curses.initscr()
    curses.curs_set(0)                  # Hide the cursor

    for l in FILE:
        File += l

    try:
        with open(File, 'r') as file:   # Open and read file line by line
            lines = file.readlines()
    except FileNotFoundError:           # Error for incorrect file location or name
        print("File not found.")
        return

    while True:

        event = keyboard.read_event()
        height, width = C.getmaxyx()    # retrieves the most current size of the terminal window

        C.clear()                                       # Clear the screen before displaying new lines

        for i in range(L, min(L + height, len(lines))): # Sets up the amount of lines to be viewed pwe page
            try:
                C.addstr(i - L, 0, lines[i])
            except curses.error:                    # Error handling for librabrary fuction miscues
                pass  

        C.refresh()

        ch = G()

        if ch == event.event_type == 'esc':         # Press the escape key to exit
            break
        elif ch == curses.KEY_DOWN:                 # Press the down arrow key to scroll down
            L = min(L + 1, len(lines) - height)
        elif ch == curses.KEY_UP:                   # Press the down arrow key to scroll
            L = max(0, L - 1)
    curses.endwin()
    #curses.wrapper()
