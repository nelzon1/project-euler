# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 16:05:59 2016

@author: jaken
"""
import numpy as np
def quad(n,a,b):
    return n**2 + a * n + b

import math as m

def isprime(num):
    if num < 2:
        return 0
    for i in range(2,int(m.sqrt(num))+1):
        if num%i==0:
            return 0
    return 1     

answergrid = np.zeros(shape=(2001,2001))

for i in range (-1001,1000):
    for j in range (-1001,1000):
        count = 0
        for n in range (0,200):
            if isprime(quad(n,i,j)):
                count += 1
        answergrid[i+1000,j+1000] = count
                
max(answergrid)
np.argmax(answergrid)               
