#!/usr/bin/python3
from pathlib import Path
import os, getopt, sys

def LSL(**kwargs):
    L = os.listdir()
    print(L)

def LS(**kwargs):
    """ Main funtion for the implemented ls command """
    F_it = {'l': False, 'a': False, 'h': False}
    #print(os.listdir())
    flags = kwargs.get('DS.flags', None)
    
    if flags == None:
        print(os.listdir())
           # in {'l': None,'a': None,'h': None}:
    elif flags in F_it:
        if flags == '-l':
            F_it ['l'] = True
            print("This is for L")
        elif flags == '-a':
            F_it ['a'] = True
            print("This is for A")
        elif flags == '-h':
            F_it ['h'] = True
            print("This is for H")

                        # for DS.flags in['l','a','h']:
                        # if '-l' in DS.flags:
                        #     print("doing a long listing")
                        # elif '-a' in DS.flags:
                        #     print("printing hidden files")
                        # elif '-h' in DS.flags:
                        #     print("human readable")
        



        #['-l'=False "-h"=False "-a"=False]

    # flags == kwargs.get('DS.flags', None)
    # if flags == None:
    #     print(os.listdir())
    # else:
    #     for flags in ['l','a','h']:
    #         if flags == 'l':
    #             print("This is for L")
    #         if flags == 'a':
    #             print("This is for A")
    #         if flags == 'h':
    #             print("This is for H")
    
    # options given from the command line is set to True
    #opts, kwargs = getopt.getopt(kwargs,"a, F, h, l, S",[])
    # except getopt.GetoptError as e:    	
    #     print_illegal_option(e.opt)
    #     usage()
    #     sys.exit(2)
    # , kwargs in opts:
    #     if opt == '-a':
    #         Op["a"] = True
    #     elif opt == '-F':
    #         Op["F"] = True
    #     elif opt == '-h':
    #         Op["h"] = True
    #     elif opt == '-l':
    #         Op["l"] = True
    #     elif opt == '-S':
    #         Op["S"] = True
