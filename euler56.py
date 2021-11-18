# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 20:21:08 2017

@author: jaken
"""

import math as m
maximum = 0
for i in range (1,100):
    for j in range (1,100):
        if sum([int(x) for x in str(i**j)]) > maximum:
            maximum = sum([int(x) for x in str(i**j)])
            winners = (i,j)
            
print (winners)
print(maximum)