# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 19:19:21 2019

@author: jaken
"""

def reflect(a,b):
    return (a - 2*b - b**2) / (b**2 - 2 * a * b - 1)

def slope(x,y):
    return -4 * x / y

def intersect(m,b):
    # m
    x=m**2 + 4
    y=2 * b * m
    z=b**2 - 100
    d=y**2 - 4*x*z
    if d < 0:
        return -99,-99
    return (-1 * y + d**(1/2)) / 2 / x, (-1 * y - d**(1/2)) / 2 / x

def ellipse(x):
    y = (100 - 4 * x**2)**(1/2)
    return y,-1*y