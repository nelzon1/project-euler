# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 21:21:18 2016

@author: jaken
"""

from collections import Counter
import math as m
import itertools as it
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
    
    
primes = prime_list(15000)

def list_prime_factors(n):
    temp = n
    results=[]
    while temp not in primes:
        for p in primes:
            if temp%p==0:
                results.append(p)
                temp/=p
                break
    results.append(int(temp))
    return results

def simplify_prime_factors(factors):
    histo = Counter(factors)
    results = []
    for f in histo:
        results.append(f**histo[f])
    return results    



#tt = simplify_prime_factors(list_prime_factors(1024))

#print(tt)
rolling_set = [[]]
rolling_set.append([])
rolling_set.append([2])
for i in range(3,100000):
    #tt = simplify_prime_factors(list_prime_factors(i))
    distinct = True
    length = True
    rolling_set.append(simplify_prime_factors(list_prime_factors(i)))
    workset=rolling_set[i-3:i+1]
    for factor in list(it.chain.from_iterable(workset)):
        if workset.count(factor) > 1:
            distinct = False            
            break
    for n in range (0,4):
        if len(rolling_set[i-n]) != 4:
            length = False
            break
    if distinct and length:
        print (i,i-1,i-2,i-3)
        break
    else:
        distinct = True
        length = True
    
        












