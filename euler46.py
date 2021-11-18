# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 00:29:57 2016

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
    
def prime_list(n):
    result = [2]
    primes = 0
    number = 3
    while  primes < n:
        if isprime(number):
            result.append(number)
            primes+=1
        number+=2
    return result
    
primes = prime_list(10000)
composites = []
num = 9
for n in range(1,10000):
   
    if not isprime(num):
        composites.append(num)
    num+=2
        
        
for p in composites:
    for q in primes:
        if q >= p:
            print (p)
            break
        if m.sqrt(0.5*(p-q))  % 1 ==0:
            break
            finished = True
        
