# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 16:44:54 2017

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


def totient(n):
    num = 1;
    denom = 1;
    for x in list(set(list_prime_factors(n))):
        num*=(x-1)
        denom *= x
    return int(num * n / denom)
    
for x in range(2,10):
    print(x, totient(x))


maximum = 2    
index = 2
maxtote=1
for x in range(2,101):
    totes = totient(x)    
    if x/totes > maximum:
        maximum = x/totes
        index = x
        maxtote=totes
        print (x, totes, maximum)