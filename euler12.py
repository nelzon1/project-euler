# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 23:36:47 2016

@author: jaken
"""
max_triangle = 100000

def trinumber (index):
    count = 0
    for i in range (1,index+1):
        count += i
    return count

def num_divisors(int1):
    count = 2
    for j in range(2,int(int1/2)+1):
        if int1%j==0:
            count += 1
    return count
ndmax=0
triangle = 0
index = 0
for i in range(index+1,max_triangle):
    triangle += i
    nd=num_divisors(triangle)
    if  nd > ndmax:
        ndmax=nd
    if nd > 200:
        break
    
    
print ( triangle , num_divisors(triangle))