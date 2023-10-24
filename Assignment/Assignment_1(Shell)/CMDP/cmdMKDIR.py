#!/usr/local/bin/python3

""" Main funtion: for the implementation of the mkdir (Make Directory) a File command """

##################################### __mkdir__ ##################################
##################################################################################

import os
import posixpath

def mkDir(**kwargs):        # Make Directory command

    dir = ""
    directory = ""
    Path = str
    d = kwargs.get('params',None)                   # Pulls the list of params for the funtion to utilize

    for e in d:                                     # Changes the list into a string
        dir += e

    print("\n\ndir:", dir)                          # New directory to be made in current directory
    
    directory = os.getcwd()                         # Only makes a directory inside the current directory
    print("directory:", directory)

    try:
        Path = (directory + "/" + dir)              # Strings are combined to make one directory string
        P = os.mkdir(Path)                          # os.mkDir takes directory string to make a new directory
        print(P)
        return
    except OSError as Error:                        # for errors
        print("Error: Directory already exists")


# if __name__ == "__main__":
#     mkDir()
