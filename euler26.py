# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 20:44:46 2016

@author: jaken
"""
from collections import Counter

def find_repetition(p):
    """ Returns a lookup dictionary for repetitions. """ 
    lookup = Counter()
    while len(p) != 0:
        for i in range(len(p)):
            lookup[p[0:i]] += 1
        p = p[1:]
    return lookup

def repeats(p):
    a = find_repetition(p)
    rs = [i for i in a if a[i] > 1][1:]
    return [r for r in rs if r*2 in p]

def long_division_inverse(integer):
    decimals = []
    zero_count=0
    numerator=10
    i=0
    while (i<(2*integer-3) and zero_count  < 11):
        y=int(numerator/integer)
        if y == 0:
            y=int(numerator/integer*10)
            decimals.append("0")
            if y == 0:
                y=int(numerator/integer*100)
 #               decimals.append("0")
 #               if y == 0:
 #                   y=int(numerator/integer*1000)
 #                   decimals.append("0")
        else:
            decimals.append(str(y))
        z = numerator % integer     

        if z == 0:
            break
        else:
            numerator = z*10
        
        i += 1
    return ''.join(decimals)
    
maxlength=1
for i in range(2,1000):
    candidates = repeats(long_division_inverse(i))
    if not candidates:
        continue
    else:
        length = len(max(candidates))
    if length > maxlength :
        maxlength = length
        d = i
        
print(d,length)