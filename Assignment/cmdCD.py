#! /user/bin/python3
import os
from Parse import ParseCmd

def cd(**kwargs):
    par = ""
    params = kwargs.get('params')
    
    for ele in params:
        par += ele
       
    print("\n Par list:", par)

    P = os.getcwd()
    print(P)
    
    print(os.chdir(par)) #'/home/jtnealley0101/shell/SHELL/CMDP/'))
    
    N = os.getcwd()
    print(N)    

