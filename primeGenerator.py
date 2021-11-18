# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 21:35:35 2017

@author: jaken
"""
import math as m
import time
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
        while num < n:
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

start = time.clock()
n=100000000
primes = set(primesToN(n))
print(time.clock() - start)
data = open('primesII.csv','w')
pp = list(primes)
pp.sort()
data.writelines(pp)
data.close()