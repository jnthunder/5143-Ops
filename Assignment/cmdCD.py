#! /user/bin/python3
import os

def CD(**kwargs):
    print("yes....")
    

    #cmd = kwargs.get('DS.cmd', None)
    #params = kwargs.get(DS.params)
    #print(params)
    #print(cmd='DS.cmd')
    #print(params='DS.params')

    P = os.getcwd()
    print(P)
    print(P)
    #flags = kwargs.get('flags', None)
    #O = kwargs.get(kwargs)
    
    #print("Current working directory is: {0}".format(os.getcwd()))
    #O = os.getcwd()
    print(os.chdir('/home/'))     #('/home/jtnealley0101/shell/SHELL/CMDP/'))
    N = os.getcwd()
    print(N)
    #print(P)
    #print("Current working directory now is: {0}".format(os.getcwd()))
    # Directory = os.getcwd()
    # print("Directory Changed to:", Directory)
    #print("Yes")

    #params = '/user/bin'
    # old = os.chdir(params)
    # print (old)
    # try:
    #     if os.chdir('params/'):
    #         print (params)
    #     if os.chdir('../'):
    #         print (params)
    #     if os.chdir('~/'):
    #         print (params)
    # except:
    #     print("Unsuccesful")
    # new = os.getcwd()
    #print (f"{new}")

# cwd(**kwargs):
#      """Concatenate files and send to std out"""
#      command = ["getcwd"]
#      if "params" in kwargs:
#        params = kwargs["params"]
#      command.extend(params)
#      callable(command)
