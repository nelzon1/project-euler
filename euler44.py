# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 23:21:13 2016

@author: jaken
"""
import math as m
def pentagon(n):
    return int( n*(3*n - 1) / 2)
    
def pentagonal (num):
    solution1 = (0.5 + m.sqrt(0.25 + 6*num) ) / 3 
    solution2 = (0.5 - m.sqrt(0.25 + 6*num) ) / 3 
    if (solution1 % 1 == 0 and  solution1 >= 1 ):
        return 1
    elif (solution2 % 1 == 0 and  solution2 >= 1 ):
        return 1
    else:
        return 0

pent = []
pentagonal(1)
pentagonal(5)

for i in range(1,1000000):
    pent.append( pentagon(i) )
diff = 500000000
for p in pent:
    for q in pent:
        if p == q:
            break
        if pentagonal(int(m.fabs(p-q))) and pentagonal(p+q):
            if m.fabs(p-q) < diff:
                diff = m.fabs(p-q)
                
print(diff)