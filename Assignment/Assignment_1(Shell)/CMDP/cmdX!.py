"""Using an exclamation point followed by a number.
   can also run the last executed command directly without knowing its history number.
   History expansion
"""
import sys
from cmdHISTORY import * #printHistory

#without parameters the history file is referenced with 
# the associated line numbers
# def history(hist):
#     lineNum = 1
#     #opens a read only version of file
#     myFile = hist
#     file = open(myFile, "r")
#     commands = file.readlines()                  #List of commands
#     for c in commands:
#         sys.stdout.write("\r"+ str(lineNum) + " " + c)
#         lineNum += 1
#     file.close()

# !!
def lastCommand(hist):
    lineNum = 1
    with open(hist, "r") as myFile:
        commands = myFile.readlines()                  #List of commands
        lineNum = len(commands)
        sys.stdout.write("\r"+ commands[lineNum-1])

# !n or !-1
def findCommand(hist,lineNum):
    with open(hist, "r") as myFile:
        commands = myFile.readlines()                  #List of commands
        sys.stdout.write("\r"+ commands[lineNum-1])

# !-n
def goBack(hist, displacement):
    with open(hist, "r") as myFile:
        commands = myFile.readlines()                  #List of commands
        lineNum = len(commands)
        #checks that displacement is not out of range
        if displacement < lineNum:
            sys.stdout.write("\r"+ commands[lineNum-displacement])  

# !string
def searchString(hist, string):
    with open(hist, "r") as myFile:
        commands = myFile.readlines()                  #List of commands
        #sys.stdout.write("\r"+ commands[lineNum-1])


if __name__=='__main__':
        
        printHistory()
        print("\n")
        lastCommand("history.txt")
        print("\n")
        findCommand("history.txt",3)
        #print("\n")
        #goBack("history.txt",2)
