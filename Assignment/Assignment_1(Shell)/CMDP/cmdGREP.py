#!/usr/local/bin/python3

""" Main funtion: for the implementation of the GREP a File command """

##################################### __grep__ ###################################
##################################################################################

import os
import glob

def grep(**kwargs):

    G = ""

    GREPP = kwargs.get('params')                                        # pulls the list of params for the funtion to utilize                                      
    print(GREPP[1])

    # String for searching in file
    with open(GREPP [1], 'r') as gf:                                    # Opens doc to read only and set to a variable
        lines = gf.readlines()                                          # Read all lines using readline()
        for row in lines:                                               # Loop to check entire file
            r = row.lower()                                             # Converts str to all lower case letters
                        
            G = GREPP[0]                                                
            print(G)
            if r.find(G)!= -1:                                          # Finds variable and returns -1 if value not found          
                print('True: found in line Number:', lines.index(row))  # if found returns index of occurrence
            else:
                print("False")                                          # If Not found
    print("\n")
    return
