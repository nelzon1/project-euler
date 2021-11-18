# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 22:33:43 2018

@author: jaken
"""
#
#for each number:
#get its prime factorization (sorted)
#start with the largest factor
#find chains that multiply to the target
#see if they add to the target, and if not, add necessary 1s
#store along with others in the same length in  a central dictionary
N = 100000


import itertools as it

def all_subsets(ss):
    return it.chain(*map(lambda x: it.combinations(ss, x), range(1, len(ss))))

def primeSieve(n):
    primes = [[x,True] for x in range(0,n+1)]
    for i in range(2,n//2+1):
        temp = 2*i
        while temp <= n:
            primes[temp][1] = False
            temp += i
    sieve = [x[0] for x in primes if x[1]]
    return sieve[2:]


## Uncomment line below if running for the first time
#MASTERPRIMELIST = primeSieve(1000000)

def powerFactor(num):
    temp = num
    factors = []
    primes = [x for x in MASTERPRIMELIST if x < (num // 2)] #primeSieve(num//2)
    index = 0
    while temp not in primes:
        try:
            curPrime = primes[index]
        except IndexError:
            break
        if temp % curPrime == 0:
            factors.append(curPrime)
            temp /= curPrime
            continue
        else:
            index += 1
    factors.append(int(temp))
    return factors
    
print ( powerFactor(179))
#dictionary = {}
#
#for n in range ( 1, 12):
#    

def superFactor(num):
    factorlist = all_subsets(powerFactor(num))
    factors = set([1])
    for sub in factorlist:
        prod = 1
        for factor in sub:
            prod *= factor
        factors.add(prod)
    return sorted(list(factors))

def chain(num):
    theChain = [num]
    nextItem = sum(superFactor(num))
    while nextItem <= N:
        if nextItem == theChain[0]:
            return theChain
        elif nextItem == 1 or nextItem == theChain[-1]:
            return []
        theChain.append(nextItem)
        nextItem = sum(superFactor(nextItem))
    return []

chain(25)



candidates = []
maximum = 0
for i in range( 10 , N):
    candidates.append([chain(i),i])
    if len(candidates[-1][0]) >= maximum:
        maximum = len(candidates[-1][0])
        print(candidates[-1])
    
