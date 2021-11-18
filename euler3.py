# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 22:40:25 2016

@author: jaken
"""
import math as m
n = 600851475143
def isprime(num):
    for i in range(2,int(m.sqrt(num))+1):
        if num%i==0:
            return 0
    return 1  

def biggest_prime_factor(number):
    notmax=1
    n=number
    prime_factor=2
    while(notmax):
        for i in range(2,n+1):
            if n%i==0 and isprime(i)==1:
                if(i>prime_factor):                
                    prime_factor = i
                n /= i
                n=int(n)                
                if n==1:
                        notmax=0
                break
    return prime_factor
    
 
prime_factor = biggest_prime_factor(n)         
    
print (prime_factor)