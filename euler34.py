# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 23:26:19 2016

@author: jaken
"""

import math as m
x=[]
for i in range (0,100000):
    number = str(i)
    total = 0
   
    for j in range (0,len(number)):
        total += m.factorial(int(number[j]))
        
    if total == i:
        x.append(i)

print (x)