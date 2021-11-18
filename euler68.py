# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 12:16:04 2017

@author: jaken
"""

import itertools as it

total = 7

nums = [1,2,3,4,5,6,7,8,9,10]

sol_16 = set()
sol_17 = set()
#for total in range(14,22):
for s in it.permutations(nums):
    rotten = False
    z1 = [str(s[5]) , str(s[0]) , str(s[1])]
    z2 = [str(s[6]) , str(s[1]) , str(s[2])]
    z3 = [str(s[7]) , str(s[2]) , str(s[3])]
    z4 = [str(s[8]) , str(s[3]) , str(s[4])]
    z5 = [str(s[9]) , str(s[4]) , str(s[0])]
    z = [z1,z2,z3,z4,z5]
    total = sum([int(x) for x in z1])
    for zz in z[1:]:
        if sum([int(x) for x in zz]) != total:
            rotten = True
            break
    
    if not rotten:
        numbers = [int(''.join(t)) for t in z]
        index = numbers.index(min(numbers))
        string = ''
        for i in range(index,index+5):    
            string += ''.join(z[i%5] )
            
        if len(string) ==16:
            sol_16.add((int(string),total))
            
        if len(string) == 17:
            sol_17.add((int(string),total))
            
print (list(sol_16))
print(list(sol_17))