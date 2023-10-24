#!/usr/bin/env python
"""
This file is about using getch to capture input and handle certain keys 
when the are pushed. The 'command_helper.py' was about parsing and calling functions.
This file is about capturing the user input so that you can mimic shell behavior.

"""
import os
import sys
from time import sleep
#from CMDP import pwd

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
      print (f"CmdParts: [cmd:{self.cmd}, directives:{self.directives}, params:{self.params}, flags:{self.flags}, stdin:{self.stdin}]")
      print("done")
      return (f"CmdParts: [cmd:{self.cmd}, directives:{self.directives}, params:{self.params}, flags:{self.flags}, stdin:{self.stdin}]")
  
  # def __repr__(self):
  #   return self.__str__()

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
    self.allCmdsDict = {'cmd':None, 'params':[],'flags':[],'directives':[]}
  
    for cmd in self.cmd:        # for each cmd in the list of cmds
      p = CmdParts()           # create an instance of the command class
      cmd = cmd.split()         # split the individual command on spaces
      p.cmd = cmd[0]            # pulls out the command from the split string 
      self.allCmdsDict['cmd'] = p.cmd

      # iterate over the rest of that command (which is really a list now)
      for c in cmd[1:]:
        if '-' in c:                    # Checks for '-' for identifying flag?
          p.flags.append(c.lstrip('-'))
          self.allCmdsDict['flags'].append(c.lstrip('-'))
        else:                           # else it's a parameter
          p.params.append(c)
          self.allCmdsDict['params'].append(c)

      p.flags = ''.join(p.flags)        # make the flags list a simple string
      self.allCmds.append(p)            # appends the object to a list
      return self.allCmdsDict
      
        
  def checkRedirect(self,cmd=None):
      """ Checks if the command has a redirect (>) """
      if not cmd:
        cmd = self.cmd.strip()
      if '>' in self.cmd:               # confirms you redirect to a file
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
    print("\n",cmd)
    return cmd 


# # p = ParseCmd('ls -l -a -h /usr/bin | wc -l | sort')
# #print('ls -l -a -h /usr/bin | wc -l | sort')
# p = ParseCmd('pwd | ls /home/jt -l | grep txt | wc -l')
# print("\n" 'ls /home/jt -l | grep txt | wc -l')
# ##print("Inputted CMD location: ", p)
# #print("Parsed CMD Locations: ", (f"{p.allCmds}"))

# print("\n")
# for  F_IT in p.allCmds:
#   # if  F_IT.cmd == 'pwd':
#   #   pwd()
#   if  F_IT.cmd == 'ls':
#     if 'l' in  F_IT.flags:
#       print("doing a long listing")
#     if 'a' in  F_IT.flags:
#       print("printing hidden files")
#     if 'h' in  F_IT.flags:
#       print("human readable")
#   # elif  F_IT.cmd == 'wc':
#   #   if 'l' in  F_IT.flags:
#   #     print("printing num lines")
#   # elif  F_IT == 'wc':
#   #   if 'l' in  F_IT.flags:
#   #     print("printing num lines")
