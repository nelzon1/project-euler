# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 12:24:07 2016

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
primas=[]
primes = 0
num = 11 
while (primes <= 10):
    fwd = str(num)
    bckwd = str(num)
    for i in range (0,len(str(num))):
        if ((not isprime(int(fwd)) or (not isprime(int(bckwd))))):
            break
        fwd=fwd[1:]
        bckwd=bckwd[:len(bckwd)-1]
    else:
        primes += 1
        primas.append(num)
    num+=1
        
        
print(primas)
print(sum(primas))