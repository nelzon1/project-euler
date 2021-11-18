# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 15:47:31 2016

@author: jaken
"""
import math as m
import itertools as it
from collections import Counter



def rotate(l, n):
    return l[n:] + l[:n]      

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
    
for i1 in range(1000,9999):
    i#1 = 1487
    TEST = it.permutations(list(str(i1)))
    cand=[]
    
    for perm in TEST:
        num = int(''.join(perm))
        if isprime(num) and num not in cand :
            cand.append(num)
         
    differences = {}
    #print(cand)
    cand.sort(reverse=True)
    for c in cand:
        for d in cand:
            if (c-d) > 0:
                differences[c,d] = c-d
    #differences.sort()           
    #for key in sorted(differences, key=differences.get):
    #    print ("{} {}".format(key, differences[key]))
        
    #need to find pairs with same difference AND repeats in the numbers
        
    for x in differences:
        for y in differences:
            if differences[x]==differences[y] and (x[0]==y[1] \
            or x[1]==y[0])\
            and len(str(x[0])) == 4 and len(str(x[1])) == 4 and len(str(y[0])) == 4 and len(str(y[1])) == 4:
                print ("{} {}".format(x, differences[x]))
                print ("{} {}".format(y, differences[y]))