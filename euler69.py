# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 21:19:32 2017

@author: jaken
"""
import math as m

def list_prime_factors(n):
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
    
def isprime(num):
    if num < 2:
        return 0
    for i in range(2,int(m.sqrt(num))+1):
        if num%i==0:
            return 0
    return 1      
    
def relative_primes(a,b):
    afac=list_prime_factors(a)
    bfac=list_prime_factors(b)
    for x in afac:
        if x in bfac:
            return False
    return True
    
for i in range(2,11):
    print(str(i) + ': ', end='')
    for j in range (2,i):
        if relative_primes(i,j):
            print(str(j) + ', ', end='')
    print('')

def totient(n):
    count=1
    for i in range(2,n):
        if relative_primes(i,n):
                count += 1
    return count
    
totient(6)
tmax=[1,1]
for x in range (2,1000000):
    t= totient(x)
    if x/t > tmax[1]:
        tmax = [x,x/t]
print( tmax)