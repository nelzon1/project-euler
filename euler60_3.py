# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 18:06:49 2017

@author: jaken
"""
import math as m

def prime_concat(a,x):
    if isprime(int(str(a) + str(x))) and isprime(int(str(x) + str(a) )):
        return True
    return False

def make_pairs(a):
    pairs = set()
    for x in working_set[a+1:]:
        if isprime(int(str(a) + str(x))) and isprime(int(str(x) + str(a) )):
            pairs.add(int(x))
    return pairs
    
    
def isprime(num):
    if num < 2:
        return 0
    for i in range(2,int(m.sqrt(num))+1):
        if num%i==0:
            return 0
    return 1    
    
    
with open('primesII.csv', 'r') as data:
    primes = [str(x)[:-1] for x in data.readlines()]

max_value = 10**12   
working_set = [int(x) for x in primes[:2500]]
pairs = [[] for i in range(len(working_set))]
for a in range(3,len(working_set)):
    if working_set[a] * 5 > max_value:
        break
    if pairs[a] == []:
        pairs[a] = make_pairs(a)
        
        
        for b in range(a+1,len(working_set)):         
            if working_set[a] + working_set[b] * 4 > max_value:
                break            
            if working_set[b] not in pairs[a]: continue
            if pairs[b] == []:
                pairs[b] = make_pairs(b)    
            
            for c in range(b+1,len(working_set)):
                if working_set[a] + working_set[b]  + working_set[c] * 3 > max_value:
                    break
                if working_set[c] not in pairs[b] or working_set[c] not in pairs[a]: continue
                if pairs[c] == []:
                    pairs[c] = make_pairs(c)
                    
                    
                for d in range(c+1,len(working_set)):
                    if working_set[a] + working_set[b]  + working_set[c] + working_set[d] * 2  > max_value:
                        break
                    if working_set[d] not in pairs[b] or working_set[d] not in pairs[a] or working_set[d] not in pairs[c]: continue                    
                    if pairs[d] == []:
                        pairs[d] = make_pairs(d)
                                       
                    
                    for e in range(d+1,len(working_set)):            
                        if working_set[a] + working_set[b]  + working_set[c] + working_set[d]  + working_set[e] >= max_value:
                            break      
                        if working_set[e] not in pairs[a] or working_set[e] not in pairs[b] or  working_set[e] not in pairs[c] or working_set[e] not in pairs[d]: continue         
                            
                        if working_set[a] + working_set[b]  + working_set[c] + working_set[d]  + working_set[e] < max_value:
                            max_value = working_set[a] + working_set[b]  + working_set[c] + working_set[d]  + working_set[e]
                            print(working_set[a] , working_set[b] , working_set[c] , working_set[d] , working_set[e], max_value)