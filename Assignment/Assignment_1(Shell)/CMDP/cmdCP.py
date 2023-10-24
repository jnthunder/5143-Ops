#!/usr/local/bin/python3

""" Main funtion: for the implementation of the cp Copy File command (from current directory) """

###################################### __cp__ ####################################
##################################################################################

import os
import shutil

def cp(**kwargs):

    Cp = "" 
    CP = kwargs.get('params')
    P = CP

    first, *rest = P                # Each string placed against a variable
    first                           # File
    rest                            # Destination

    for r in rest:                  # Seperates the String from the list format
        Cp += r

    SRC = first                     # File to be copied
    print("\nFile copied:", SRC)

    DEST = Cp                       # Destination of copied file
    print("Directory copied to:", DEST)
    shutil.copy(SRC, DEST)          # The shutil module utilizes the file found in the current directory,
                                    # makes a copy of it and puts it into the desired location.
    print("\n")
    return
