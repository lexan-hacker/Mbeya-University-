# simple file detection using python

import os

path = "C:\\Users\\HP\\Desktop\\try.py"

path2 = "C:\\Users\\HP\\Desktop\\storefront"

if os.path.exists (path) :
    print( " The file path that you had specified exists so don't worry ")
    
    if os.path.isfile (path) :
        print( " The path that you have provided is a file , so dont worry ")
        
    else :
        print ( " Probably it isn't a file , try again later ")
    
else :
    print( " Soory ! The path file doesn't exist ")
    
    
if os.path.exists (path2) : 
    print ( " The path specified exists and it is a directory for now for more look down ")
    
    if os.path.isdir (path2) :
        print( " The path is a directory ")
        
    else : 
        print ( "Something went wrong ")
        
else : 
    print ( " Sometging went wrong , please try again later ")

