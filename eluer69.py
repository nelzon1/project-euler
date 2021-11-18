# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 11:27:49 2017

@author: jaken
"""
import math as m

def gcf(a,b):
    d = 0
    while (a%2==0 and b%2==0):
        a/=2
        b/=2
        d+=1
    while a != b:
        if a%2==0:
            a/=2
        elif b%2==0:
            b/=2
        elif a > b:
            a = (a-b)/2
        else:
            b = (b-a)/2
    g = int(a)
    return g * 2**d
    
def totient(a):
    t = 1
    if a % 2 == 1:
        t+=1
    for i in range (3,a):
        if gcf(i,a)==1:
            t+=1
    return t


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

totients = []
answers = [] 
t2 = []   
for z in range(2,100):
    prod = 1
    totients.append(totient(z))
    answers.append(z/totients[-1])
    for x in map(lambda x: x-1,list_prime_factors(z)):
        prod *= x
    t2.append(prod)