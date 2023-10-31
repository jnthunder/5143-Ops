#!/usr/local/bin/python3

""" Main funtion: for the implementation of the Head a File command """

#################################### __chMod__ ###################################
##################################################################################

import os

def chMod(**kwargs):

    f = ""
    MOD = 0
    S = int
    CHMOD = kwargs.get('params')      # pulls the list of params for the funtion to utilize

    S = CHMOD[0]                        # grabs out the first param
    F = CHMOD[1]                        # grabs out the second param
    f = os.path.abspath(F)              # grabs the path and appends it to the file name

    if S =='000':                       # Checks if triple zero was entered and returns an error
        print("Error removal of all permissions unauthorized")
        return
    
    try:                                # This is the first thing to check
        C = int(S, 8)                   # changes the string to the required int
        os.chmod(f, C)                  # takes the variables given and changes the files permisions

    except ValueError:                  # If the value entered is incorrect the error message is returned
        print("Invalid Mode. Please review permissions before next attemp.")
        return
