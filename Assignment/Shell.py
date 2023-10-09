#!/usr/local/bin/python3
"""
This file is about using getch to capture input and handle certain keys 
when the are pushed. The 'command_helper.py' was about parsing and calling functions.
This file is about capturing the user input so that you can mimic shell behavior.

"""
import os
import sys
from time import sleep
from Getch import Getch
#from CMDP import *
from cmdLSL import LSL, LS
from cmdPWD import PWD
from cmdCD import CD


##################################################################################
##################################################################################

# getch = Getch()                             # create instance of our getch class
# prompt = "$"                               # set default prompt

###################################### print_cmd #################################
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

###################################### print_cmd #################################
##################################################################################

def print_cmd(cmd):
    """ This function "cleans" off the command line, then prints
        whatever cmd that is passed to it to the bottom of the terminal.
    """
    padding = " " * 80
    sys.stdout.write("\r"+padding)
    sys.stdout.write("\r"+prompt+cmd)
    sys.stdout.flush()

getch = Getch()                             # create instance of our getch class
prompt = "$"                               # set default prompt

##################################################################################
##################################################################################

if __name__ == '__main__':
    ParseCmd

    cmd = ""                                # empty cmd variable
    print_cmd(cmd)                          # print to terminal
    
    while True:                             # loop forever
        char = getch()                      # read a character (but don't print)

        if char == '\x03' or cmd == 'exit': # ctrl-c
            raise SystemExit(" Bye.")
        
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
                print_cmd(cmd)
                sleep(0.3)
                #cmd = cmd[:-1]
                
            if direction in 'B':            # down arrow pressed
                # get the NEXT command from history (if there is one)
                # prints out 'down' then erases it (just to show something)
                cmd += u"\u2193"
                print_cmd(cmd)
                sleep(0.3)
                #cmd = cmd[:-1]
            
            if direction in 'C':            # right arrow pressed    
                # move the cursor to the right on your command prompt line
                # prints out 'right' then erases it (just to show something)
                cmd += u"\u2192"
                print_cmd(cmd)
                sleep(0.3)
                #cmd = cmd[:-1]

            if direction in 'D':            # left arrow pressed
                # moves the cursor to the left on your command prompt line
                # prints out 'left' then erases it (just to show something)
                cmd += u"\u2190"
                print_cmd(cmd)
                sleep(0.3)
                #cmd = cmd[:-1]
            
            print_cmd(cmd)                  # print the command (again)

        elif char in '\r':                  # return pressed 
            
            p = ParseCmd(cmd)
            (f"{p.allCmds}")

            # splits on spaces
            print(cmd.split())

            # check if redirect to std out is in the string
            if '>' in cmd:
                # confirms you redirect to a file
                cmd = cmd.split('>')

            print(cmd)

            # split command if any `pipes` exist
            cmds = cmd[0].split('|')

            print(cmds)

            # iterate over individual commands
            for cmd in cmds:
                print(cmd.split())
    
            print("\n")
            for DS in p.allCmds:
                                # if DS.cmd ():
                #     get.cmd()
                if DS.cmd == 'CD': #and DS.directives == 'kwargs':
                    print(cmd)
                    CD()
                    
                    # params = DS.params
                    # print(params)
                    # print(DS.params)
                    # CD(params) 
                    
                    
                    #params = DS.params
                    #CD()
                    
                # elif DS.cmd == 'LS':
                #     LS(flags = 'DS.flags', params = 'DS.params')

                elif DS.cmd == 'LSL':
                    print(DS.cmd)
                    LSL()

                elif DS.cmd == 'LS':
                    #if DS.flags == None:
                    LS(DS.flags)
                    
                    # for DS.flags in['l','a','h']:
                    #     if '-l' in DS.flags:
                    #         print("doing a long listing")
                    #     elif '-a' in DS.flags:
                    #         print("printing hidden files")
                    #     elif '-h' in DS.flags:
                    #         print("human readable")
                
                elif DS.cmd == 'Ls':
                    ls()
                    # for DS.flags in['l','a','h']:
                    #     if '-l' in DS.flags:
                    #         print("doing a long listing")
                    #     elif '-a' in DS.flags:
                    #         print("printing hidden files")
                    #     elif '-h' in DS.flags:
                    #         print("human readable")
                # elif DS.cmd == 'wc':
                #         if 'l' in DS.flags:
                #             print("printing num lines")       #kwargs=DS.cmd
                    #len(DS.len)
                    #LS(kwargs=LS(DS.flags))
                    #LS(kwargs=LS(f"{p.allCmds}"))
                    
                    
                    # DS.len = None
                    #LS(DS.flags)


                    # if ''in DS.flags:          #This prints for ls with or without flags
                    #     print(os.system('ls'))
                    # if 'l' in DS.flags:
                    #     print(os.system('ls -l'))
                    # if 'a' in DS.flags:
                    #     print(os.system('ls -a'))
                    # if 'h' in DS.flags:
                    #     print(os.system('ls -h'))
                    
                elif DS.cmd == 'mkDir':
                    mkDir()

                elif DS.cmd == 'mv':
                    if '' in DS.params:
                        print(os.system('mv'))

                elif DS.cmd == 'CP':
                    CP()

                elif DS.cmd == 'PWD':
                    print(DS.cmd)
                    PWD()

                elif DS.cmd == 'cp':
                    
                    # if 'kwargs = [0]' in DS.params:
                    print("now")
                    print(os.system('cp'))
                    # else:
                    #     print("now1")    
                
                elif DS.cmd == 'wc':
                    if 'l' in DS.flags:
                        print("printing num lines")

             #     sleep(1)    


            cmd = ""                        # reset command to nothing (since we just executed it)
            print_cmd(cmd)                  # now print empty cmd prompt
        else:
            cmd += char                     # add typed character to our "cmd"
            print_cmd(cmd)                  # print the cmd out
