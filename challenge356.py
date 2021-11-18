# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 23:36:55 2018

@author: jaken
"""

#SEND + MORE = MONEY
import string
inputstr = "SEND + MORE = MONEY"
inputstr = inputstr.replace('+','')
inputstr = inputstr.replace('=','')
words = inputstr.split()

def grind(key):
    #final = key.pop()
    
    for i in range (0,17):
        for alpha in string.ascii_uppercase[i:i+10]:
            
            for x in range(0,10):
            
                for word in key:
                    word.replace(alpha,str(x))
                    
        
grind(words)