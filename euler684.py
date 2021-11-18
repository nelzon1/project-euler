# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 20:17:31 2020

@author: jaken
"""

"""
Euler 684

smallest number that has a digit sum of x, is equal to:
    
    divide by 9, find remainder
    that many 9 digits, preceeded by remainder
    
sum those from 1 to k

fibbonaci sequence here is:
    
    0, 1, 1, 2, 3, 5, 8, 11 etc
    
need sum of sum from 1 to k for 2 <= i <= 90 for fibbonaci numbs

finally, modulo 1 000 000 007

"""

fibb = [0,1]

for i in range (2,91):
    fibb.append( fibb[-1] + fibb[-2] )


    
def euler684(n):
    a = n // 9
    b = n % 9
    return int(str(b) + a*'9') % 1000000007

def euler684_sum(k):
    total = 0
    for i in range (1, k+1):
        total += euler684(i)
        
    return total

bigsum = 0
'''
for x in fibb[2:]:
    bigsum += euler684_sum(x) % 1000000007
    
print (bigsum)

print(bigsum % 1000000007)
'''