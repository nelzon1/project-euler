# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 22:07:56 2018

@author: jaken
"""

def isBouncy(num):
    lastDigit = int(str(num)[0])
    direction = 0 #can be -1, 0, 1 for forwards/backwards and initial =0
    for digit in str(num)[1:]:
        digit = int(digit)
        if direction == 0:
            if digit > lastDigit:
                direction = 1
                lastDigit = digit
                continue
            elif digit < lastDigit:
                direction = -1
                lastDigit = digit
                continue
            else:
                direction = 0 # go to next digit
                lastDigit = digit
                continue
    
        elif direction == 1:
            if digit >= lastDigit:
                lastDigit = digit
                continue
            else:
                return True

        elif direction == -1:
            if digit <= lastDigit:
                lastDigit = digit
                continue
            else:
                return True
            
    return False

ratio = 0
bouncy = 0
num = 1
while ratio < 0.99:
    if isBouncy(num):
        bouncy += 1
        ratio = bouncy / num
    num += 1
    
num -= 1
print ("num:" , num)
print ("bouncy: ", bouncy)
print("ratio: ", ratio)
    