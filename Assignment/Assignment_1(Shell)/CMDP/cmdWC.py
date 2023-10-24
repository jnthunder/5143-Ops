"""The Linux wc command calculates a file's word, 
    line, character, or byte count.
"""
import os

def wc(**kwargs):
    
    # creating variable to store the
    # number of words
    number_of_words = 0
    infileName = ""
    lineCount = 0
    byteCount = 0
    D = kwargs.get('params')
    for C in D:
        infileName += C    
    
    with open(infileName,'r') as file:
        #return the absolute path of the file
        path = os.path.abspath(infileName)
        #counts the bytes in the file
        byteCount = os.path.getsize(path)
        print("Path: ", path)
        print("File Name: ", infileName)
        print("byteCount: ", byteCount)
        # Reading the content of the file
        # using the read() function and storing
        # them in a new variable
        data = file.read()

        # Splitting the data into separate lines
        # using the splitlines() function
        lineCount = len(data.splitlines())
        print("lineCount: ", lineCount)
        # Splitting the data into separate words
        # using the split() function
        words = len(data.split())
        print("words Count: ", words)
        # Printing total number of words
        #print(lineCount, words, byteCount, infileName)

        
if __name__=='__main__':
    wc('TopScoreFile.txt')
