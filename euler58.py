# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 23:41:52 2017

@author: jaken
"""

import math as m

def isprime(num):
    if num < 2:
        return 0
    for i in range(2,int(m.sqrt(num))+1):
        if num%i==0:
            return 0
    return 1     
    
def next_diag( term ):
    if term[0]==1:
        return (2,3)
    return (term[0]+1,term[1] + 2 * m.ceil((term[0] )/4) )
    
side_length = 7

diagonals = [(1,1)]
count = 1
primecount = 0
ratio = 1.0
while ratio > 0.1:
    for i in range(4):
        diagonals.append(next_diag(diagonals[len(diagonals)-1]))
        if isprime(diagonals[len(diagonals)-1][1]):
            primecount+=1
        count += 1
    ratio = primecount/count
print (ratio)
print (max(diagonals))
print ((diagonals[len(diagonals)-1][0]-1)/2 + 1)