# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 18:51:57 2017

@author: jaken
"""

def size(n):
    return len(str(n))
count = 1 
for i in range (2,100):
    for j in range(1,100):
        if size(i**j) == j:
            print (i,j,i**j)
            count += 1
print(count)
            
