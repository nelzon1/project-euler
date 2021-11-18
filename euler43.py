# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 22:54:15 2016

@author: jaken
"""
import itertools as it

def nodupes(num):
    dupe = []
    for digit in str(num):
        if (digit in dupe):
            return 0
        dupe.append(digit)
    if len(dupe) > 10:
        return 0
    return 1
    
pandigitals = it.permutations(['1','2','3','4','5','6','7','8','9','0'])
total=0

def tests(num):
    if not int(''.join(num[1:4])) % 2 == 0:
        return 0
    if not int(''.join(num[2:5])) % 3 == 0:
        return 0
    if not int(''.join(num[3:6])) % 5 == 0:
        return 0
    if not int(''.join(num[4:7])) % 7 == 0:
        return 0
    if not int(''.join(num[5:8])) % 11 == 0:
        return 0
    if not int(''.join(num[6:9])) % 13 == 0:
        return 0
    if not int(''.join(num[7:10])) % 17 == 0:
        return 0
    return 1

tests('1406357289')

for number in pandigitals:
    if tests(number):
        total += int(''.join(number))