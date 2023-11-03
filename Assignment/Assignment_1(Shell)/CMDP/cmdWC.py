"""The Linux wc command calculates a file's word, 
    line, character, or byte count.
"""
import os

def wc(**kwargs):
    
    # creating variable to store the
    # number of words
    number_of_words = 0
    F = ""
    Lines = 0
    WC = kwargs.get('params')
    F = WC[0]
    # for C in WC:
    #     F += C    
    
    with open(F,'r') as file:
        #return the absolute path of the file
        path = os.path.abspath(F)
        #counts the bytes in the file
        byteCount = os.path.getsize(path)
        #print("Path: ", path)
        #print("File Name: ", F)
        # Reading the content of the file
        # using the read() function and storing
        # them in a new variable
        data = file.read()

        # Splitting the data into separate lines
        # using the splitlines() function
        Lines = len(data.splitlines())

        # Splitting the data into separate words
        # using the split() function
        words = len(data.split())
        print("File Name: ", F)
        print("Lines: ", Lines)
        print("words Count: ", words)
        print()
        return words
        # Printing total number of words
        #print(Lines, words, F)

        
if __name__=='__main__':
    wc('TopScoreFile.txt')
