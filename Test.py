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
    if char == '\x03' or cmd =='exit':      # Pressed 'Control + c' command
        raise SystemExit(" Goodbye!")       # raise and SystemExit are Base exception code products and
                                            # allow us to exit a program and provides a return to the system
    elif cmd == "CH":
        print (CH())

    elif char == '\x7f':                    # Pressed backspace button command
        cmd = cmd[:-1]

    elif char == '\x1b':                    # Pressed Arrow key (part of what is needed)
        null = Getch()                      
        direction = Getch()                 # Pulls the Unicode from the corresponding pressed arrow button

        if direction in 'Uup':              # Up Arrow goes to previously entered command(s)
            cmd += u"\u2191"
            print_cmd(cmd)
            sleep(0.5)
            cmd = cmd[:-1]                  # Removes the arrow from the terminal after a the sleep time count

        if direction in 'Ddown':
            cmd += u"\u2193"
            print_cmd(cmd)
            sleep(0.5)
            cmd = cmd[:-1]

        if  direction in 'Rright':
            cmd = u"\u2192"
            print_cmd(cmd)
            cmd = cmd[:-1]

        if direction in 'Lleft':
            cmd = u"\u2190":
            print_cmd(cmd)
            sleep(0.5)
            cmd = cmd[:-1]

    """ If command exists, it is executed"""
    elif char in '\r':
         if CH.excists(cmd):                                    
            CH.invoke(cmd = cmd, params = params, threads = False)
            print_cmd(cmd)
            sleep(0.5)

    """ If command doesn't exist, the printout executes and shows the user the cmd attempted"""
    else:
          print (" ERROR command %s doesn't exist") % (cmd))
          sleep (0'5)
