# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 22:11:54 2017

@author: jaken
"""
import itertools
#import math
def cubes(n):
    num = 1
    while num < n:
        yield num**3
        num+=1
        

for cube in cubes(100000):
    count = 0
    #cube = 41063625 
    #cube = 56623104 
    #cube = 66430125 
    for z in set(list( itertools.permutations(str(cube)))):
        decimal = int(''.join(z))**(1/3) % 1.
    
        if z[0]==0:
            continue
        if (decimal < 10**(-7)) or (decimal > 0.999999999 and decimal < 1.0 ) :
            count+=1
    if count == 5:
        print (cube)


#solution = 10403062487 ??

'''
for q in cubes(100):
    count = 0
    for p in cubes(100):
        if len(str(p)) < len(str(q)):
            continue
        elif len(str(p)) > len(str(q)):
            break
        else:
            for z in itertools.permutations(str(q)):
                if int(''.join(z)) == p:
                    count += 1
                    break
    if count == 5:
        print (q)
'''