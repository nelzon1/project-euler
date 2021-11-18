# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 19:57:55 2017

@author: jaken
"""
import math


def palindrome(number):
    for i in range(0,int((len(number))/2)):
        if number[i] != number[len(number)-1-i]:
            return 0
    return 1
    
count = 0
i=1
total = 0

while(i < 10000):
    if count == 0:
        num = i
    rev = int(str(num)[::-1])
    num+= rev
    if palindrome(str(num)):
        i+=1
        count = 0
        total += 1
    elif count > 50:
        i+=1
        count = 0
    else:          
        count += 1
        
print(9999-total)