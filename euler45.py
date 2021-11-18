# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 16:23:54 2016

@author: jaken
"""

def triangle(n):
    return int( n * (n + 1) / 2)
    
def pentagonal(n):
    return int( n*(3*n - 1) / 2)
    
def hexagonal(n):
    return int( n*(2 * n - 1))
    
tri = []
pent = []
hexa = []

for i in range(1,1000000):
    tri.append( triangle(i) )
    pent.append( pentagonal(i) )
    hexa.append( hexagonal(i) )
    
answers = set.intersection(set(tri),set(pent),set(hexa))

print (answers)