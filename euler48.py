# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 23:49:00 2016

@author: jaken
"""

import math as m
num = 0
for i in range(1,140):
    num += m.pow(i,i)
    
print (num)