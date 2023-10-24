"""""$rm [OPTION]... FILE.."""""
import os

def rm(**kwargs):
    #user specified file
    inFileName = kwargs.get('params')
    fileName = inFileName
    #absolute path of file
    pathname = os.path.abspath(fileName)
    #directory
    dirname = os.path.basename(os.path.split(pathname)[0])
    #print('/' + dirname + '/...')
    #print(pathname)
    #If the specified path matches the path of an existing 
    #file in the directory, remove the path
    if os.path.exists(pathname):
        if os.path.split(pathname)[0].endswith(dirname):
            print("Hello")
            #os.remove(pathname)
    else:
        #if the file is not in the current directory
        #os.walk is used to search a given path 
        #to find the matching file
        for root, dirs, files in os.walk(r'C:\Users'):
            for name in files:
            
                # As we need to get the provided python file, 
                # comparing here like this
                if name == fileName:  
                    #file path to be removed
                    print(os.path.abspath(os.path.join(root, name)))
                    #os.remove(os.path.abspath(os.path.join(root, name)))
            
if __name__=='__main__':
    rm("test.txt")
#Collapse
