import os
import sys
import threading
import stat
import time
from Getch import Getch


"""Define Commands"""

def exit(**kwargs):
  sys.exit()


"""Classes"""

"""This sets up the shells helper function"""
class CommandHelper(object):
  def __init__(self):
    self.commands = {}

def invoke(self):
  if "cmd" in kwargs:
    cmd = kwargs["cmd"]
  else:
    cmd = ""
  
  if "params" in kwargs:
    params = kwargs["params"]
  else:
    params = []

  if "thread" in kwargs:
    thread = kwargs ["thread"]
  else:
    thread = False

  if command not in self.command:
    print: ("Command not found, try another command")
  elif not thread:
    self.command [cmd](*params)
  else:
    if len(params) > 0:
      c = threading.Thread(target = self.commands[cmd], args = params(kwargs))
    else:
      c = threading.Thread(target = self.commands[cmd])

    c.start()
    c.join()

"""Clears CMD line, then prints the passed cmd whatever cmd is passed in at the bottom of the terminal"""
def print_cmd(cmd):
  padding = " " * 80
  sys.stdout.write("\r" + padding)
  sys.stdout.write("\r" + prompt + cmd)
  sys.stdout.flush()

def exists(self, cmd):
  print (self.commands)
  return cmd in self.commands


"""MAIN"""

if __name__ == "__main__":

  CH = CommandHelper()
  char = Getch()
  prompt = "$: "

  cmd = ""                                  # Empty command variable
  print_cmd(cmd)                            # Print to terminal

  while True:
    if char == '\x03' or cmd =='exit':      # control c
        raise SystemExit(" Goodbye!")       # raise and SystemExit are Base exception code products and
                                            # allow us to exit a program and provides a return to the system
    elif cmd == "CH":
      print (CH())

    elif char == '\x7f':                    # back space
      cmd = cmd[:-1]
      
  
