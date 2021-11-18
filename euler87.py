# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 18:46:24 2017

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

def primesToN(n):
        yield 2
        num = 3
        while num <= n:
            if isprime(num):
                yield num
                num+=2
            else:
                num+=2

def nPrimes(n):
        count = 1
        yield 2
        num = 3
        while count < n:
            if isprime(num):
                yield num
                num+=2
                count +=1
            else:
                num+=2    
                
combos = [(x**2,y**3,z**4) for x in primesToN(7072) for y in primesToN(369) for z in primesToN(85)]

sums = 0
chcksums = set()
for z in combos:
    if sum(z) < 50000000:
        chcksums.add(sum(z))    
print (len(chcksums))