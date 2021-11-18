# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 16:57:14 2017

@author: jaken
"""
import itertools as it

import math as m

def isprime(num):
    if num < 2:
        return 0
    for i in range(2,int(m.sqrt(num))+1):
        if num%i==0:
            return 0
    return 1    

def list_prime_factors(n):
    if n == 1:
        return [1]
    temp = n
    results=[]
    while not isprime(temp):
        for x in range(2,int(m.sqrt(temp))+1):       
            if isprime(x) and temp % x ==0:
                results.append(x)
                temp/=x
                break
    results.append(int(temp))
    return results


def totient(n):
    num = 1;
    denom = 1;
    for x in list(set(list_prime_factors(n))):
        num*=(x-1)
        denom *= x
    return int(num * n / denom)
    

minimum = 2    
index = 2
mintote=1
for x in range(2,10000000):
    totes = totient(x)    
    perms = set(map(lambda x: ''.join(x) ,it.permutations(list(str(x)))))
    if str(totes) in perms:
        if x/totes < minimum:
            minimum = x/totes
            index = x
            mintote=totes
            print (x, totes, minimum) 
    
    