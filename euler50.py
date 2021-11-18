# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 21:45:22 2016

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
    primes = 1
    number = 3
    while  primes < n:
        if isprime(number):
            result.append(number)
            primes+=1
        number+=2
    return result

primes = prime_list(78499)

#primes = prime_list(17000)
maxlength = 1
maxprime = {'prime':2,'length':1}
for n in primes[primes.index(777737):]:
    subset = primes[:int(primes.index(n)/80)]
    for x in subset:
        prime_sum = 0
        count=0
        for y in subset[subset.index(x):]:
            prime_sum += y
            count+=1
            if prime_sum == n:
               if maxprime['length'] < count:
                   maxprime['prime'] = n
                   maxprime['length'] = count
            if prime_sum > n:
                break
            
            
print(maxprime)
#{'length': 543, 'prime': 997651}
"""
for n

generate list of primes up to n

for each prime: sum along prime list until equal or greater

"""