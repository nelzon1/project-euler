# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 21:51:33 2017

@author: jaken
"""

def root_step(x):
    return [x[1] + 2*x[0],x[0]]
    
def square_root(n):
    if n == 1:
        return [3,2]
    seed = [5,2]
    for i in range (1,n-1):
        seed=root_step(seed)
    return [sum(seed),seed[0]]
    
count = 0

for i in range (1,1001):
    temp = square_root(i)
    if len(str(temp[0])) > len ( str ( temp[1]) ):
        count += 1
        
print (count)