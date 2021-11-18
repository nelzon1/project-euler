# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 22:04:24 2016

@author: jaken
"""
def char_position(letter):
    return ord(letter) - 96

def namescore(name_in):
    name = name_in.lower()
    name_score = 0
    for char in name:
        name_score += char_position(char)
    name_score *=  (namelist.index(name_in) )    
    return name_score    
namesum = 0

namelist=[]
data = open('euler22.csv','r')
readline=" "
while readline != "":
    readline = data.readline().rstrip()

    namelist.append(readline)
namelist.sort()
for name in namelist:
    namesum += namescore(name)
    t=1

            
