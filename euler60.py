# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 09:22:46 2017

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
   
primes = prime_list(1000)
primes=primes[1:]
sets = it.combinations(primes,3)

#one set that works: [3, 7, 109, 673, 129976621]
#another 4-set: (23, 311, 677, 827)

#'''
pair_sets=[]
for s in sets:
    broken=False 
    for p in it.permutations(s,2):
        
        if not isprime(int(''.join(str(x) for x in p))):
            
            broken=True            
            break
            
    if not broken:
        pair_sets.append(s)
        #print (s)
        #break
#'''




'''
s = [23, 311, 677, 827,3]
#s = [3,7,109, 673]
no_solution = True
while no_solution:
    if  not isprime(s[4]):
        s[4]+=2
        continue
    broken=False 
    for p in it.permutations(s,2):
        
        if not isprime(int(''.join(str(x) for x in p))):
            
            broken=True            
            break
            
    if not broken:
        print (s)
        break
    s[4]+=2
'''