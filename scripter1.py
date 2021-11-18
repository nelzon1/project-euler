# -*- coding: utf-8 -*-
"""
Created on Tue May 23 22:11:45 2017

@author: jaken
"""
import os, time, sys
print(sys.argv)

try:
    fileLoc = sys.argv[1]
except:
    sys.exit("Error: No file argument specified. Use 'python " + sys.argv[0] + " <filename>'")
    
    
age = time.time() - os.path.getmtime(fileLoc)

print (round(age,1))