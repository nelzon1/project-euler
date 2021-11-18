# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 21:18:42 2017

@author: jaken
"""
import math as m

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

def primesToN(n):
        yield 2
        num = 3
        while num <= n:
            if isprime(num):
                yield num
                num+=2
            else:
                num+=2

def isprime(num):
    if num < 2:
        return 0
    for i in range(2,int(m.sqrt(num))+1):
        if num%i==0:
            return 0
    return 1      
    
primes=primesToN(100000)

#n=100

def frac(n):
    fractions = set()
    for i in range(2,n+1):
        for j in range(1,i):
            unique = True
            primes = primesToN(int(m.sqrt(j)) +1)
            for k in primes:
                if ((i%k==0) and (j%k==0)) or (i%j==0 and j!=1):
                    unique = False                    
                    break
            if unique:
                fractions.add((j,i))
                #if k > j: 
                #    break
    return len(fractions)
print(frac(10))
x=frac(2)     
for i in range(2,61):
    y=x
    x=frac(i)
    
    print(str(i) + '\t: ' + str(x) + '\t' + str(x-y))
    