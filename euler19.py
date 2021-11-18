# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 23:50:24 2016

@author: jaken
"""

months = [31,28,31,30,31,30,31,31,30,31,30,31]

day = 1# Monday = Dec 31 1900
year = 1901
count = 0
for i in range(1,100):
    for j in range(0,12):
        if j ==1 and year%4==0:
            day += 29
        else:
            day += months[j]
        if day % 7 == 0:
            count += 1
    year += 1        
print (count)