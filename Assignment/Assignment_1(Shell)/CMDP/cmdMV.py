#!/usr/local/bin/python3

""" Main funtion: for the implementation of the Head a File command """

###################################### __mv__ ####################################
##################################################################################

import os
import shutil

def mv(**kwargs):

    Mv = "" 
    Move = kwargs.get('params')         # pulls the list of params for the funtion to utilize
    V = Move
    first, *rest = V                    # Each string is placed against a variable
    first                               # file
    rest                                # destination

    print("\ntxt:", first)
    print("\nrest:", rest)

    for r in rest:                      # Changes the list into a string
        Mv += r
    
    O = os.getcwd()                     # Gets and sets the CWD to a Variable
    SRC = O + "/" + first               # Both CWD and file string combined
    print(SRC)
    DEST = Mv                           # Requested destination string
    print(DEST)
    shutil.move(SRC, DEST)              # Shutil module utilized to move the file

