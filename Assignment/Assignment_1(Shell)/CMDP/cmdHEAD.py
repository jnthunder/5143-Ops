#!/usr/local/bin/python3

""" Main funtion: for the implementation of the Head a File command """

##################################### __head__ ###################################
##################################################################################

import os

def head(**kwargs):

    HD = ""
    HEAD = kwargs.get('params')                 # pulls the list of params for the funtion to utilize

    first, *rest = HEAD                         # Each string is placed against a variable
    first                                       # File
    rest                                        # Number of lines

    for E in first:                             # Seperates the String from the list format
        HD += E

    n = int("" .join(map(str, rest)))           # Sets the requirements and number for the search

    with open(HD, "r") as f:                    # Opens file and sets to read only
        #f = open(HD, "r")

        print("\n", f.readlines(100*n), "\n")   # Prints out the requested (amount) lines

    return
