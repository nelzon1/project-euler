# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 21:17:07 2016

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
#primes = prime_list(7849)
results = { 'key' : bin(127) , 'list' : [] , 'prime' : 2, 'length':2}
for p in primes:
    if len(results['list']) == 8:
        break
    
    for n in range (1,2**len(str(p))-1):
        binrep = str(bin(n))[2:]
        
        if len(binrep) < len(str(p)):
            for z in range ( len(str(p)) - len(binrep) ):
                binrep = '0' + binrep
        number = str(p)
        temp = []
        prime_count = 0
        for x in range(0,10):
            
            index = 0            
            
            for bit in binrep:
                
                if int(bit) == 1:
                    digits = [int(z) for z in number]
                    digits[index] = x                 
                    number = ''.join([str(z) for z in digits])
                index += 1
            
            if isprime(int(number)) and number[0] != '0':
                prime_count += 1
                if number not in temp:
                    temp.append(number)
        if prime_count > results['length']:
            results['key']=binrep
            results['list']=temp
            results['prime']=p
            results['length']=prime_count

print(results)