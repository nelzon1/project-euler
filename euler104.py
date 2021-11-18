# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 17:30:53 2018

@author: jaken
"""

def fibb(n):
    if n == 1 or n == 2:
        return 1
    val1 = 1
    val2 = 1
    for i in range(n-2):
        temp = val2
        val2  = val1 + val2
        val1 = temp
        
    return val2

def lastPan(num):
    digits = set()
    for digit in str(num)[-9:]:
        if digit != '0':
            digits.add(digit)
    if len(list(digits)) == 9:
        return True
    else:
        return False
    
def firstPan(num):
    digits = set()
    for digit in str(num)[0:10]:
        if digit != '0':
            digits.add(digit)
    if len(list(digits)) == 9:
        return True
    else:
        return False
    
val1 = 1
val2 = 1
count = 2
while (1==1):
    temp = val2
    val2  = val1 + val2
    val1 = temp
    count += 1
    if (lastPan(val2) and firstPan(val2)):
        break
    
print (count, val2)