# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 19:56:10 2018

@author: jaken
"""

def rectangles(x,y,a,b):
    if x == 1 and y == 1:
        return a * b
    elif x==1:
        return ( (a - x + 1) * (b - y + 1) ) + rectangles(x,y-1,a,b)
    return ( (a - x + 1) * (b - y + 1) ) + rectangles(x-1,y,a,b)
        

#print ( rectangles(2,3,2,3) ) 

def rerec(a,b):
    recs = 0
    for i in range(a,0,-1):
        for j in range(b,0,-1):
            recs += (a - i + 1) * (b - j + 1)
            
    return recs

solns = [1]

for x in range (1,1000):
    for y in range(1,x+1):
        recs = rerec(x,y)
        if abs(2000000 - recs) < 2000000 - solns[-1]:
            solns.append(recs)
print(solns)