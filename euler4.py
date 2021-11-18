# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 22:22:27 2016

@author: jaken
"""
def palindrome(number):
    for i in range(0,int((len(number))/2)):
        if number[i] != number[len(number)-1-i]:
            return 0
    return 1


biggest = 1
for i in range(1,1000):
    for j in range(1,1000):
        num = i * j
        string = str(num)
        if palindrome(string)==1 and num > biggest:
            biggest = num
            
print(biggest)
        
        
        