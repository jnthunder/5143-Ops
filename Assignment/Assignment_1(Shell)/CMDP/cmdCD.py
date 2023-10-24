#!/usr/local/bin/python3

""" Main funtion: for the implementation of the cd Change Directory command """

############################ __Change_Directory__ ################################
##################################################################################

import os

def cd(**kwargs):                               # Moves in and out of directories

    C = ""
    CD = kwargs.get('params')               # sets the list of of strings to a variable

    for D in CD:                            # Changes the list into a string
        C += D
 
    P = os.getcwd()                         # Retrieves current directory
    print("\nPrevious Directory:", P)
    
    if C == "~":                            # Changes directory to the home directory
        os.chdir("/home")

    elif C == "..":                         # Changes directory to the parent directory of the current directory
        p = os.path.abspath(os.path.join(P, os.pardir))
        os.chdir(p)

    else:                                   # Changes the directory to the requested directory
        os.chdir(C)
        
    print("Current Directory:", os.getcwd(), "\n")
    return    
