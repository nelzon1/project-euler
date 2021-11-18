# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 16:57:59 2020

@author: jaken
"""

import math as m

def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

def pro_factor(n):
    factors = [1,n]
    for i in range (2,int(m.sqrt(n)) + 1):
        if n % i == 0:
            factors.append(i)
            if int(n/i) != i:
                factors.append(int(n/i))
    factors.sort()            
    return factors

PRIME_LIST = primes(100000000)

def divprime(d, n):
    if (d + (n/d)) in PRIME_LIST:
        return True
    else:
        return False
    
N = 100000000

goodguys = []

for i in range (2,N):
    good = True
    factors = pro_factor(i)
    if len(factors)%2 == 1:
        continue
    for x in factors[:int(len(factors)/2)]:
        if x + i/x not in PRIME_LIST:
            good = False
            break 
    if not good:
        continue
    goodguys.append(i)
            

print(len(goodguys))
print("Sum:", sum(goodguys))
