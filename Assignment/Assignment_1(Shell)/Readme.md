# Advanced Operating Systems
# Project 1: Shell

## Authors:  James Nealley
##          Khetha Kunene

### Key Advisor:  Dr. Terry Griffin

### Key Contributions:  Dr. Griffin (Getch, Parser and Shell Starter Code)
###                    Bing AI, 'https://www.bing.com/'
###                    ChatGPT, 'https://chat.openai.com/'
###                    Digital Ocean, 'https://www.digitalocean.com/community/tutorials'
###                    flexiple, 'https://flexiple.com/python/python-append-to-string'
###                    Free Code Camp, 'https://www.freecodecamp.org'
###                    Geeks for Geeks, 'https://www.geeksforgeeks.org'
###                    How to Forge, 'https://www.howtoforge.com/tutorial'
###                    How-to Geak, 'https://www.howtogeek.com'
###                    julia, 'https://docs.julialang.org/en/v1/stdlib/REPL/'
###                    Learn Data Sci, 'https://www.learndatasci.com/solutions/python-move-file/'
###                    List of Unicode Symbols, 'https://symbl.cc/en/unicode/table/'
###                    PYnative Python Program, 'https://pynative.com/python-delete-files-and-directories/'
###                    Python 3.12.0 Documentation, 'https://docs.python.org'
###                    Python for Beginners, 'https://www.pythonforbeginners.com/'
###                    Real Python, 'https://realpython.com'
###                    Stack Exchange, 'https://unix.stackexchange.com/'

### Search Engines:  bing
###                 Firefox
###                 Google

## Purpose
This shell was developed by using Visual Studios and Python Code.  It's main purpose was to serve as a learning tool for understanding how develop and utilize a shell interface. Among the techniques learned from this project was; how to develop a set of commands capable of working with a database by retrieving data, passing data, and developing data. 

Below is a brief overview of the top level shell behaviors covered in this shells development:
- After start-up processing, your program repeatedly should perform these actions:
    - Print to stdout a prompt consisting of a percent sign followed by a space.
    - Read a line from stdin.
    - Lexically analyze the line and create an array of command parts (tokens). 
    - Syntactically analyze (i.e. parse) the token array to form a command.
    - Once identified, the proper command is executed:
        - It creates a child process by duplicating itself.
        - The overloaded process receives all the remaining strings given from a keyboard input (if necessary), and starts a command execution.

This project also served a secondary purpose of learning how to utilize python coding and WSL in Visual Studios.  Main parts of Python learned from this project are the basic building blocks (def, loops, variables, etc..), opening, reading, creating files, passing commands and data between functions and files, parsing, key reading and assigning (unicode) and many more. 


### Requirements

Below is the list of requirements given to develop the shell
- language of implementation will be Python or C++.
- Threads (optional) 
  - use threads to execute each command.
  - You should wait for the thread to complete, before returning control to the main process (unless specified to run in background via the ampersand (&)).
- Each command returns a string
- Each command should have the ability to accept input from another command
- Your shell must support the following types of commands:

>1. The internal shell command "exit" which terminates the shell.
    - **Concepts**: shell commands, exiting the shell
    - **System calls**: `exit()`
1. A command with no arguments
    - **Example**: `ls`
    - **Details**: Your shell must block until the command completes and, if the return code is abnormal, print out a message to that effect.
    - **Concepts**: Forking a child process, waiting for it to complete, synchronous execution
2. A command with arguments
    - **Example**: `ls -l`
    - **Details**: Requires parsing string into components. We will discuss multiple ways of capturing input (ex Getch, sys.argv)
    - **Concepts**: Command-line parameters 
3. A command, with or without arguments, whose output is redirected to a file
    - **Example**: `ls -l > foo`
    - **Details**: This takes the output of the command and put it in the named file
    - **Concepts**: File operations, output redirection
5. A command, with or without arguments, whose input is redirected from a file
    - **Example**: `sort < testfile`
    - **Details**: This takes the named file as input to the command
    - **Concepts**: Input redirection, more file operations
6. A command, with or without arguments, whose output is piped to the input of another command.
    - **Example**: `ls -l | more`
    - **Details**: This takes the output of the first command and makes it the input to the second command
    - **Concepts**: Pipes, synchronous operation

- All return values must checked and handled correctly. Determining what the possible return values are, what errors they indicate, and what you must do when you get that error.

Additionally, implementing a command must be done without making a call to the existing shell:
```python
from subprocess import call

call(["ls", "-l"])

```
The above implementation of the `ls` command with the `-l` flag, is NOT an implementation. It is a "system" call to the existing shell. I also do not expect your python implementation of the `ls` command to be as extensive as this: http://www.pixelbeat.org/talks/python/ls.py.html . Your implementations should be somewhere in between. 



### How to utilize the codes developed for this shell


| Name | Command | Information |
| ---- | ------- | ----------- |
| Concantinate | cat file file | More files may be added if desired |
| Change Directory | cd path | Path must be in line with the current parent directories |
| Change Permissions | chmod ### file | numbers are a range between 0, 1, 4, 6 and 7 with zero's giving you an Error |
| Copy File | cp file destinationpath | Same as above for change directory rules concerning direct path |
| Grep a Word | Grep word file | |
| Head of File | head file # | # represents the amount of lines you would like to veiw from the top of the selected file |
| History | history | Shows a list of previously called commands |
| Page Read a File | less (Page up "n", Page down "m", To exit "q") | Reads the size of the screen and breaks the file down into these portions for viewing with m, n and q used to control going between pages and exit |
| List Files | ls | Can use the following flags in any combonation to retrieve a listing of the current directories files (-l, -a, -h, -la, -lh and -lah |
| LS Flag | - l | Retrieves a long listing or deteailed break down of the files located in the current directory |
| LS Flag | - a | Retrieves any hidden files located in the current directory |
| LS Flag | - h | Makes the Listing Human readable (main purpose is for utilization with long listing (ls -l) as ls itself doesn't show the properties requiring -h |
| Make Directory | mkdir name | Whatever is used as the 'name' position in this command will become the directories name |
| Move File | mv file destination-path | This will grab the file entered and place it in the directory under the same branch as the current directory |
| Current Working Directory | pwd | This will display the path of the directory your currently working in |
| Remove File | rm file | This command without any flags will delete requested file. 'rm' may use either of the following flags for removing a Directory |
| Remove Directory | -r | This flag added to 'rm' will remove the requested directory if it doesn't contain any files |
| Remove Directory | -rf | !CAUTION! This flag added to 'rm' will delete a directory even though it is not empty !CAUTION! |
| Sort | sort file | will sort out the contents of a file and print to screen |
| Tail of File | tail file # | # represents the amount of lines you would like to veiw from the end of the selected file |
| Word Count | wc file | Will return the number a word is found in the file (This takes into account the spelling and upper and lower case used in the word) |
