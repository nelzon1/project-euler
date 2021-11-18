# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 23:57:51 2016

@author: jaken
"""
from math import sqrt

def F(n):
    return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))
    
print (F(5))