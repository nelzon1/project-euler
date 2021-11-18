# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 21:16:51 2016

@author: jaken
"""
import math as m

def char_position(letter):
    return ord(letter) - 96

def triangle (num):
    solution1 = (-1 + m.sqrt(1+8*num) ) / 2 
    solution2 = (-1 -+ m.sqrt(1+8*num) ) / 2 
    if (solution1 % 1 == 0 and  solution1 >= 1 ):
        return 1
    elif (solution2 % 1 == 0 and  solution2 >= 1 ):
        return 1
    else:
        return 0

tri=[]
for i in range (1,25):
    tri.append(int(0.5*i*(i+1)))

triangle (15)

def word_value(word):
    total = 0
    word = word.lower()
    word.replace(" ","")
    for char in word:
        total += char_position(char)
    return int(total)
    
    
word_value('sky')
total = 0
allwords=0
with open('euler42.txt','r') as f:
    for line in f:
        line = line.replace('","',' ')
        line = line.replace('"','')
        for word in line.split():
            #print(word)  
            alpha = word_value(word)
            if alpha in tri:
                total += 1
            allwords += 1
print (total)
print (allwords)