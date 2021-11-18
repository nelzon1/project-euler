# -*- coding: utf-8 -*-
"""
Created on Mon May  2 19:34:56 2016

@author: jaken
"""

"""
Return the set of proper factors (1 included)
"""
import math as m

def pro_factor(n):
    factors = [1]
    for i in range (2,int(m.sqrt(n)) + 1):
        if n % i == 0:
            factors.append(i)
            if i != n:
                factors.append(int(n/i))
    return factors
    
