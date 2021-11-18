# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 19:16:12 2017

@author: jaken
"""
import time

def gcf(a,b):
    r1 = max([a,b]) % min([a,b])
    z = min([a,b])
    while r1!= 0:
        r2=r1
        r1 = z % r1
        z = r2
    return z

start = time.clock()
count = 0   
for i in range(1,1000001):
    for j in range(1,i):
        if gcf(i,j) == 1:
            count+=1
    
print("There are " + str(count) + " elements in the set for d<=1000000")
print("Operation took " + str(time.clock() - start) + " sec.")