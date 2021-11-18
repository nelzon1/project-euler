# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 20:28:22 2016

@author: jaken
"""
n=1
condition = True
while condition:
    if set(str(n)) == set(str(2*n)) == set(str(3*n)) == \
        set(str(4*n)) == set(str(5*n)) == set(str(6*n)):
        print (n)
        break
    n+=1