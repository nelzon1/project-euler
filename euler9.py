# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 22:03:32 2016

@author: jaken
"""
triplet = [0,0,0]
for i in range (1,1001):
    for j in range (1,1001):
        k = 1000 - i - j
        if k <= 0:
            break
        if ((i**2 + j**2) == k**2):
            triplet[0]=i
            triplet[1]=j
            triplet[2]=k
            break
        
print(  triplet[0],triplet[1],triplet[2])