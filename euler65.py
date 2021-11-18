# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 23:01:09 2017

@author: jaken
"""

def gen_s(n):
    s=[]
    count =1
    for i in range(n):
        if (i+1) % 3 == 2:
            s.append(count*2)
            count+=1
        else:
            s.append(1)
    return s
    
index = 99
s=gen_s(index)
total = (1,s[-1])
count = 1

for i in range(index-1):
    total = (total[1], total[0] + total[1] * s[-2-i])
    
total = (total[0] + total[1] * 2,total[1])    

print(total)