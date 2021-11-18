# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 18:52:58 2018

@author: jaken
"""

import math
import decimal

decimal.getcontext().prec = 50

def heron(a,b,c):
    s = decimal.Decimal((a + b + c) / 2)
    return decimal.Decimal(s*(s-a)*(s-b)*(s-c)).sqrt()

totalsum = 0

for i in range(1,1000000000):
    if (i*3 + 1) > 1000000000:
        print('Exceeded 1,000,000,000 permiter')
        break
    if heron(i,i+1,i+1) % 1 == 0 :
        totalsum += i*3 + 2
        #print(i,i+1,i+1)
    if heron(i,i,i+1) % 1 == 0:
        #print(i,i,i+1)
        totalsum += i*3 + 1
        
print("Total perimiter of triangles: ",totalsum)