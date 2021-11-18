# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 20:44:46 2016

@author: jaken
"""
import numpy as np
sequenceLength=0
num=0
for i in range (2,1000):
    if sequenceLength >= i:
        break
    
    foundRemainders = np.zeros(i)
    value = 1
    position = 1
    
    while (foundRemainders[value] == 0 and value != 0):
        foundRemainders[value]=position;
        value *= 10;
        value %= i;
        position += 1;
        
    if (position - foundRemainders[value] > sequenceLength):
        sequenceLength = position - foundRemainders[value]
        num=i



