# -*- coding: utf-8 -*-
"""
Created on Sun May  8 13:32:21 2016

@author: jaken
"""

def fibb(a,b):
    return a+b
    
fibbs = [1,1]
count = 1
number = 0

while number < 10**999 :
    number = fibb(fibbs[count], fibbs[count-1])
    fibbs.append(number)
    count += 1
    
    
print(len(fibbs))
print(max(fibbs))