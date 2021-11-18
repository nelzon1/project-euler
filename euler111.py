# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 20:07:48 2018

@author: jaken
"""

def primeSieve(n):
    primes = [[x,True] for x in range(0,n+1)]
    for i in range(2,n//2+1):
        temp = 2*i
        while temp <= n:
            primes[temp][1] = False
            temp += i
    sieve = [x[0] for x in primes if x[1]]
    return sieve[2:]

import time

start = time.clock()



n = input("Value? ")
print("Prime Sieve up to " + str(n))
start = time.clock()

primeSieve(int(n))

print("Complete, time: " + str(round(time.clock() - start,5)))
