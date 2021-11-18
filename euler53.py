# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 20:43:28 2016

@author: jaken
"""
from functools import reduce
import operator as op
def ncr(n, r):
    r = min(r, n-r)
    if r == 0: return 1
    numer = reduce(op.mul, range(n, n-r, -1))
    denom = reduce(op.mul, range(1, r+1))
    return numer//denom
count=0  
combs = set()  
for i in range(1,101):
    for j in range(1,int(i)):
        t = ncr(i,j)
        if t > 1000000:
            count +=1
            combs.add(t)
print (count)
print(len(combs))