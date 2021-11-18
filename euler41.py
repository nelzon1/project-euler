# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 16:41:09 2016

@author: jaken
"""
import math as m

def nodupes(num):
    dupe = []
    for digit in str(num):
        if (digit in dupe or int(digit)>len(str(num)) or int(digit) == 0):
            return 0
        dupe.append(digit)
    return 1
    
    
def isprime(num):
    if num < 2:
        return 0
    for i in range(2,int(m.sqrt(num))+1):
        if num%i==0:
            return 0
    return 1     
    
maxnum=0
for i in range(2,1000000000):
    if (isprime(i) and nodupes(i)):
        maxnum=i
        
print(maxnum)