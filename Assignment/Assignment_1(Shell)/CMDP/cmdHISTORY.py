import sys
#from rich import print

def createhistory():
    #creating a file with the command function "w" will create a new text file
    #whether or not there already exists a file with the same name, 
    #allowing the previous file to be overwritten if it exists
    #Initialize on startup
    file = open("history.txt","w")
    #printHistory("history.txt")
    file.close()

def updateHistory(arg):
    file = open("history.txt","a")
    #writes each command to the history file when they are executed
    #command = kwargs.get()    # "hello"             #single command
    #commands = []                                  #list of commands
    file.writelines([arg,"\n"])                 #insert command
    #f.writelines(commands) #insert multiple strings to history file from a list
    file.close()
    
def history(**kwargs):
    lineNum = 1
    #opens a read only version of file
    file = open("history.txt", "r+")
    #read commands from file and print them
    #print(file.read())
    commands = file.readlines()                  #List of commands
    #print(commands)
    for c in commands:
        command = str(lineNum) + " " + c
        sys.stdout.write("\r" + command)
        lineNum = lineNum + 1      
    file.close()
    
    
# if __name__=='__main__':
    
#     createhistory()
#     updateHistory()
#     updateHistory()
#     printHistory()




# import subprocess
# import readline

# def history(**kwargs):
#     """The Main page entry for history cmd"""

#     print("\n" .join([str(readline.get_history_item(i + 1)) for i in range(readline.get_current_history_length())]))


# if __name__ == '__main__':
#     print ("\n")
#     history()
