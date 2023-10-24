#!/usr/local/bin/python3

""" Main funtion: for the implementation of the Head a File command """

##################################### __tail__ ###################################
##################################################################################

import queue

def tail(**kwargs):
    TL = ""
    L = ""
    I = 0
    Q = queue.Queue()
    TAIL = kwargs.get('params')             # pulls the list of params for the funtion to utilize

    first, *rest = TAIL                     # Each string is placed against a variable
    first                                   # File
    rest                                    # Number of lines
    
    for A in first:
        TL += A

    L = int("".join(map(str, rest)))        # Sets the requirements and number for the search

    with open(TL) as F:                     # Opens file and pulls the lines out of the file
        for line in F:                      # and sets them into a Queue
            Q.put(line.strip())
            if I >= L:
                Q.get()
            else:
                I += 1      

    for i in range(I):                      # The Queue is accessed and lines printed out
        print(Q.get())
