# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 21:35:55 2017

@author: jaken
"""
import math
total = 1
(x,y)=1,1
y=0
while total < 10**13:
    y = math.ceil((2*x*(x-1))**(1/2))
    if y*(y-1) == 2*x*(x-1):
        print (x,y)
    x+=1
    total = y