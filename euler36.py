# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 00:29:41 2016

@author: jaken
"""

def palindrome(number):
    for i in range(0,int((len(number))/2)):
        if number[i] != number[len(number)-1-i]:
            return 0
    return 1

answers = []
binanswers=[]
i=37
str(bin(i))[2:]

for i in range(1,1000000):
    if (palindrome(str(i)) and palindrome(str(bin(i))[2:])):
        answers.append(i)
        binanswers.append(str(bin(i))[2:])
        
print (answers)
print (binanswers)