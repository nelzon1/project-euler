# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 21:45:56 2016

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
  
def rotate(l, n):
    return l[n:] + l[:n]  
    
def circle_prime(num):
    n=len(str(num))
    temp=num
    for i in range (0,n):
        if not isprime(temp):
            return 0
        temp=int(rotate(str(temp),1))
        
    return 1
    
count=0
primes = []
for i in range (2,1000000):
    for digit in str(i):
        if (digit == '0'):
            break
    else:
        if circle_prime(i):
            count += 1
            primes.append(i)

    
print (count)
print (primes)