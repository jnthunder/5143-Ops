#!/usr/local/bin/python3

""" Main funtion: for the implementation of the cat(concantenate) command 2 or more files """

############################## __Concantenate__ ##################################
##################################################################################

import os

def cat(**kwargs):

    A = ""
    T = 0
    CAT = kwargs.get('params')                  # Pulls params from the shell

    C = (len(CAT))                              # Reads the amount of file names passed in

    while True:                                 # Loop reads files into a string and appends them together
        if T <= C-1:
            with open(CAT[T], 'r') as ct:       # Opens and reads file
                for CT in ct:                   # creates a string from each file and appends it in order
                    A+=CT
                    T+=1
        else:                                   # Breaks loop when the files have been concantenated
            print("\n", A, "\n")
            break
    return


""" Alternate funtion: for the implementation of the cat(concantenate) command 2 or more files """

        #CAT[T]                                             # Print out and place each param to a variable
    
    # V1 = CAT[0]
    # V2 = CAT[1]
    # V3 = CAT[2]
    
    # # Creates a new file and copies in the info from the first file
    # with open(V1, 'r') as CP1, open(V3, 'a') as CT:        
    #     for T1 in CP1:
    #         CT.write(T1)            

    # # Opens the 2nd file and appends the info to the bottom of the created fill
    # with open(V2, 'r') as CP2, open(V3, 'a+') as CT2:
    #     for T2 in CP2:
    #         CT2.write(T2)
