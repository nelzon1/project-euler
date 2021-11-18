# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 23:39:36 2016

@author: jaken
"""


import numpy as np

sum1 = 0
sum2=0

from math import sqrt
def F(n):
    return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))
x = np.arange(1,36)
y = np.arange(1,36)

for i in x:
    y=np.round(F(i), decimals=0)
    
for i in y:
    if (i % 2 == 0 and i < 4000000):
        sum2 += i    
    
for i in x:
    temp=F(i)
    fibb = np.round(temp,decimals=0)
    if (fibb % 2 == 0 and fibb < 4000000):
        sum1+= fibb


print(sum1)
print (sum2)
        