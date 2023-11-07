Project 1: Shell


How to utilize the codes developed for this shell

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
