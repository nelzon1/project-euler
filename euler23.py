# -*- coding: utf-8 -*-
"""
Created on Mon May  2 19:34:45 2016

@author: jaken
"""

import math as m

def pro_factor(n):
    factors = [1]
    for i in range (2,int(m.sqrt(n)) + 1):
        if n % i == 0:
            factors.append(i)
            if int(n/i) != i:
                factors.append(int(n/i))
    return factors
    
def abundant(factors,n):
    if sum(factors) > n:
        return True
    else:
        return False
        
abun = []

for i in range(1,28123 +1):
    factor = pro_factor(i)
    if abundant(factor,i):
        abun.append(i)
        
        
solution=[]
for i in range(1,28123 +1):
    for p in abun:
        if p > i/2:
            break
        if (i-p in abun):
            solution.append(i)
            break
        
answers=[]        
for i in range(1,28123 +1):
    if i not in solution:
        answers.append(i)
    
print( "Largest number that cannot be written as two abundants: " + str(max (answers) )    )
print( "Sum of all numbers which cannot be written as two abundants: " + str(sum (answers) )    )
"""
for i in range(1,10000):
    for p in abun:
        if p > i:
            continue
        for q in abun:
            if q > i:
                break
            if p + q == i and (i in solution) == False:
                solution.append(i)
"""