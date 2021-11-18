# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 21:56:59 2019

@author: jaken
"""
"""
#euler 111

prime runs:
    for all 10 digit primes:
        histogram them by digit
        for each repeated digit 0-9:
            loop through the set of primes and their histograms:
                track the max histogram freq
                if the element is greater, drop the current list and replace with new entry
                if the elemtn is equal, add it to the list
                if it is less, continue
                
            return the sum
            
            
"""
import time
start = time.clock()
import math

def primeSieve(n):
    primes = [[x,True] for x in range(0,n+1)]
    for i in range(2,n//2+1):
        temp = 2*i
        while temp <= n:
            primes[temp][1] = False
            temp += i
    sieve = [x[0] for x in primes if x[1]]
    return sieve[2:]
        
print("Starting prime sieve...")
primes = [x for x in primeSieve(10**7) if math.floor(math.log10(x)) == 6 ]

print("Prime sieve complete up to " + str(10**7) + ".\nTime taken: " + str(round((time.clock() - start),3)) + "s.")