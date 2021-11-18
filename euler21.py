# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 21:35:52 2016

@author: jaken
"""
import math as m
amnum = []
def amicable(a,b):
    if dsum(a) == b and dsum(b) == a and a!=b:
        return True
    else:
        return False
        
def dsum(a):
    factors = [1]
    for i in range(2,int(m.sqrt(a))):
        if a%i==0:
            factors.append(i)
            factors.append(int(a/i))
    return sum(factors)

dsum(18)  

  
for i in range(1,10000):
    for j in range(int(i/2),int(i*1.5)):
        if amicable(i,j):
            amnum.append(i)
            amnum.append(j)