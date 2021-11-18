# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 22:21:26 2017

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
    
def prime_list(n):
    result = [2]
    primes = 1
    number = 3
    while  primes < n:
        if isprime(number):
            result.append(number)
            primes+=1
        number+=2
    return result

#Euler 60

#find pairings for grouping of n up to 9999
#use groupings found to one more prime
#repeat up to n=5

primelimit=9999

primes = prime_list(1000)
primes=primes[1:]

sets = it.combinations(primes,2)
solutions=[]
pair_sets=set()
combos=sets
for x in range(4):
    if x > 0:
        combos=[z for z in pair_sets]
        pair_sets=set()
    #sets = it.combinations(primes,x)
    for s in combos:
        
        for prime in primes:
            if prime in s:
                continue
            
            temp=list(s)
            temp.append(prime)
            temp.sort()
            if tuple(temp) in pair_sets:
                continue
            
            broken=False 
            for p in it.permutations(temp,2):
                
                if not isprime(int(''.join(str(x) for x in p))):
                    
                    broken=True            
                    break
                    
            if not broken:
                pair_sets.add(tuple(temp))
                if x > 0:
                    solutions.append(temp)
                #print (s)
            #break
    
print (solutions)
test=set([3])
test.add(3)