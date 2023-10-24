#!/usr/local/bin/python3

################################# __HEADER__ #####################################
##################################################################################
# Advanced Operating Systems Shell
#
# Authors:  James Nealley
#           Khetha Kunene
#
# Key Advisor:  Dr. Terry Griffin
# 
# Key Contributions:  Dr. Griffin (Getch, Parser and Shell Starter Code)
#                     Bing AI, 'https://www.bing.com/'
#                     Digital Ocean, 'https://www.digitalocean.com/community/tutorials'
#                     flexiple, 'https://flexiple.com/python/python-append-to-string'
#                     Free Code Camp, 'https://www.freecodecamp.org'
#                     Geeks for Geeks, 'https://www.geeksforgeeks.org'
#                     How to Forge, 'https://www.howtoforge.com/tutorial'
#                     How-to Geak, 'https://www.howtogeek.com'
#                     julia, 'https://docs.julialang.org/en/v1/stdlib/REPL/'
#                     Learn Data Sci, 'https://www.learndatasci.com/solutions/python-move-file/'
#                     Python 3.12.0 Documentation, 'https://docs.python.org'
#                     Python for Beginners, 'https://www.pythonforbeginners.com/'
#                     Real Python, 'https://realpython.com'
#                     Stack Exchange, 'https://unix.stackexchange.com/'
#
# Search Engines:  bing
#                  Firefox
#                  Google
#       
#
################################# __Shell__ ######################################
##################################################################################

"""
This file is about using getch to capture input and handle certain keys when
the are pushed. The 'command_helper.py' was about parsing and calling functions.
This file is about capturing the user input so that you can mimic shell behavior.
"""
import os
import sys
from time import sleep
from Getch import Getch
from Parse import ParseCmd
from CMDP import *

getch = Getch()                             # create instance of our getch class
prompt = "$"                               # set default prompt

################################# Parse_cmd ######################################
##################################################################################

def PARSE(cmd):
    flags = []
    directives = []
    params = []
    cmd = cmd.split()
    print(cmd)
    for f in cmd:
        if '--' in f:
            directives.append(f.lstrip('--'))
        elif '-' in f:
            flags.append(f.lstrip('-'))
        elif '/' in f:
            params.append(f.lstrip('/'))

    return {'flags':''.join(flags),'directives':directives,'params':params}

################################# print_cmd ######################################
##################################################################################

def print_cmd(cmd):
    """ This function "cleans" off the command line, then prints
        whatever cmd that is passed to it to the bottom of the terminal.
    """
    padding = " " * 80
    sys.stdout.write("\r"+padding)
    sys.stdout.write("\r"+prompt+cmd)
    sys.stdout.flush()

################################### Main #########################################
##################################################################################

if __name__ == '__main__':
    
    cmd = ""
    ht = ""                                # empty cmd variable
    H = 0
    I = 0
    open('history.txt', 'a')
    createhistory                           # Creates history file
    with open("history.txt", "r") as ht:
        History = ht.readlines()
 
    print_cmd(cmd)                          # print to terminal
    
    while True:                             # loop forever
        char = getch()                      # read a character (but don't print)

        if char == '\x03' or cmd == 'exit': # ctrl-c
            #delete history file
            raise SystemExit(" Bye!")
        
        elif char == '\x7f':                # back space pressed
            cmd = cmd[:-1]
            print_cmd(cmd)
            
        elif char in '\x1b':                # arrow key pressed
            null = getch()                  # waste a character
            direction = getch()             # grab the direction
            
            if direction in 'A':            # up arrow pressed
                # get the PREVIOUS command from your history (if there is one)
                # prints out 'up' then erases it (just to show something)
                cmd += u"\u2191"
                H -= 1              # or H = H - 1 for decrementing 
                cmd = History[H]
                print_cmd(cmd)
                # sleep(0.3)
                #cmd = cmd[:-1]
                
            if direction in 'B':            # down arrow pressed
                # get the NEXT command from history (if there is one)
                # prints out 'down' then erases it (just to show something)
                cmd += u"\u2193"
                H += 1              # or H = H + 1 for incrementing
                cmd = History[H]
                print_cmd(cmd)
                #sleep(0.3)
                #cmd = cmd[:-1]
            
            if direction in 'C':            # right arrow pressed    
                # move the cursor to the right on your command prompt line
                # prints out 'right' then erases it (just to show something)
                cmd += u"\u2192"
                cmd = input[:+1]
                print_cmd(cmd)
                sleep(0.3)
                #cmd = cmd[:-1]

            if direction in 'D':            # left arrow pressed
                # moves the cursor to the left on your command prompt line
                # prints out 'left' then erases it (just to show something)
                cmd += u"\u2190"
                input = ""
                P = 0
                i=0
                for i in input:
                    I += i
                print('I')
                print(I)
                P -= 1
#                cmd = I[P]
                    
                # print_cmd(cmd)
                sleep(10.0)
                #cmd = cmd[:-1]
            
            #print_cmd(cmd)                 # print the command (again)

        # If no No arrows, delete or exit sequence, the commands are updated in history and processed
        elif char in '\r':                   
            updateHistory(cmd)              # History called and updated with cmd's
            p = ParseCmd(cmd)               # Parse is called and cmd's are broken down
            pdict = p.allCmdsDict
            #print("\n", pdict)
            for cmd in p.allCmds:           # pulls all cmd's from from Parser
                pass
                
            # Loop to call all functions requested by the user
            for F_IT in p.allCmds:

                if F_IT.cmd == 'cat':       # Concantenate
                    cat(**pdict)
                
                elif F_IT.cmd == 'cd':      # Change Directory
                    cd(**pdict)

                elif F_IT.cmd == 'cp':      # Copy File
                    cp(**pdict)

                elif F_IT.cmd == 'grep':    # Grep File
                    grep(**pdict)

                elif F_IT.cmd == 'head':    # Head of file
                    head(**pdict)

                elif F_IT.cmd == 'history': # History
                    history(**pdict) 
                                       
                elif F_IT.cmd == 'less':    # Less (Page at a time)
                    less(**pdict)

                # elif F_IT.cmd == 'ls':
                #     longListing(**pdict)

                # elif F_IT.cmd == 'lsA':
                #     ls(**pdict)

                # elif F_IT.cmd == 'lsB':
                #     lsA(**pdict)
            
                elif F_IT.cmd == 'mkDir':   # Make Directory
                    mkDir(**pdict)

                elif F_IT.cmd == 'mv':      # Move File
                    mv(**pdict)

                elif F_IT.cmd == 'pwd':     # Current Working Directory
                    pwd(**pdict)

                elif F_IT.cmd == 'rm':      # Remove Directory/File
                    rm(**pdict)

                elif F_IT.cmd == 'tail':    # End of File
                    tail(**pdict)

                elif F_IT.cmd == 'wc':      # Word Count
                    wc(**pdict)

             #     sleep(1)    

            cmd = ""                        # reset command to nothing (since we just executed it)
            print_cmd(cmd)                  # now print empty cmd prompt
        else:
            cmd += char                     # add typed character to our "cmd"
            print_cmd(cmd)                  # print the cmd out
