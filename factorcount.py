# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 00:46:56 2016

@author: jaken
"""

import math as m

def isprime(num):
    for i in range(2,int(m.sqrt(num))+1):
        if num%i==0:
            return 0
    return 1  

def prime_factors(number):
    notmax=1
    product=1
    n=number
    factors=[]
    while(notmax):
        for i in range(2,int(m.sqrt(n)+2)):
            if n%i==0 and isprime(i)==1:
                factors.append(i)

                n /= i
                n=int(n)    
                break
            if n==1:
                notmax=0
                break
            if i == int(m.sqrt(n)+1):
                factors.append(number)
                notmax=0
                break
            
    factors.sort()            
    d = {x:factors.count(x) for x in factors}
    for x in d.values():
        product *= x+1
    return product
    
n = 100000
sump = 0
maxfactors=1
for i in range (1,n):
    sump += i
    pf = prime_factors(sump)
    if pf > maxfactors:
        maxfactors = pf
        triangle = sump
        if pf > 2000:
            break
    
    
    
print(maxfactors)
print ( triangle) 