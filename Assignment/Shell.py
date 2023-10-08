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
#from Parse import ParseCmd, CmdParts
from CMDP import *
from cmdLS import ls


##################################################################################
##################################################################################

# getch = Getch()                             # create instance of our getch class
# prompt = "$"                               # set default prompt


###################################### Getch #####################################
##################################################################################

# class Getch:

#     def __init__(self):
#         try:
#             self.impl = _GetchWindows()
#         except ImportError:
#             self.impl = _GetchUnix()

#     def __call__(self):
#         return self.impl()

# class _GetchUnix:
#     def __init__(self):
#         import tty
#         import sys

#     def __call__(self):
#         import sys
#         import tty
#         import termios
#         fd = sys.stdin.fileno()
#         old_settings = termios.tcgetattr(fd)
#         try:
#             tty.setraw(sys.stdin.fileno())
#             ch = sys.stdin.read(1)
#         finally:
#             termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
#         return ch

# class _GetchWindows:
#     def __init__(self):
#         import msvcrt

#     def __call__(self):
#         import msvcrt
#         return msvcrt.getch()

# if __name__=='__main__':
#     G = Getch()

#     while(G):
#         pass


###################################### CmdParts ##################################
##################################################################################

class CmdParts:
  """ This is the docs for CmdParts """
  def __init__(self):
      self.cmd = ''
      self.directives = []
      self.flags = []
      self.params = []
      self.stdin =  None

  def __str__(self):
      return (f"CmdParts: [cmd:{self.cmd} directives:{self.directives} params:{self.params}  flags:{self.flags} stdin:{self.stdin}]")


###################################### ParseCmd ##################################
##################################################################################

class ParseCmd:
  def __init__(self, cmd=None):
    self.cmd = cmd
    self.redirect = False
    self.fileName = None
    self.cmd_list = self.cmd.split()
    self.cmd_len = len(self.cmd_list)
    self.allCmds = []
    self.run()

  def run(self):
    if not self.cmd:
      return
    
    self.checkRedirect()
    self.checkPipe()
    self.parse()
    
  def parse(self):

    allCmds = []                # list of all split commands

    for cmd in self.cmd:        # for each cmd in the list of cmds
      p = CmdParts()            # create an instance of the command class
      cmd = cmd.split()         # split the individual command on spaces
      p.cmd = cmd[0]            # pulls out the command from the split string 

      # iterate over the rest of that command (which is really a list now)
      for c in cmd[1:]:
        if '-' in c:                    # Checks for '-' for identifying flag?
          p.flags.append(c.lstrip('-'))
        else:                           # else it's a parameter
          p.params.append(c)

      p.flags = ''.join(p.flags)        # make the flags list a simple string
      self.allCmds.append(p)            # appends the object to a list
#       # loop over each command and strip extra spaces away
# i = 0
# for cmd in cmds:
#     cmds[i] = cmd.strip()
#     i += 1
# print(cmds)

# # example dictionary showing processed commands
# parts = {
#     'cmd':'',
#     'flags':'',
#     'params':''
# }
        
  def checkRedirect(self,cmd=None):
    """ Checks if the command has a redirect (>) """
    if not cmd:
        cmd = self.cmd.strip()
    elif '>' in self.cmd:               # confirms you redirect to a file
        self.cmd = self.cmd.split('>')
        self.redirect = True
        self.fileName = self.cmd[-1]
        self.cmd = self.cmd[0]
    return self.cmd
        

  def checkPipe(self,cmd=None):
    """ returns an array (list) of commands """
    if not cmd:
      cmd = self.cmd
    if '|' in cmd:
      # confirms you have a pipe
      cmd = cmd.split('|')
    else:
      self.cmd = [cmd]
      return [cmd]
    self.cmd = cmd
    return cmd 
 


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
    CmdParts
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
                    LSL()

                elif DS.cmd == 'LS':
                    #if DS.flags == None:
                    LS(DS.flags)
                    for DS.flags in['l','a','h']:
                        if '-l' in DS.flags:
                            print("doing a long listing")
                        elif '-a' in DS.flags:
                            print("printing hidden files")
                        elif '-h' in DS.flags:
                            print("human readable")
                
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
