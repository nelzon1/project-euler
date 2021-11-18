# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 21:43:29 2016

@author: jaken
"""
import numpy as np
"""
iterate, but check dictionary first. dictionary will be a numpy list

if dictionary entry is found,:
     add key value to current count,  
     update dictionary and  
     terminate loop,

as soon as the chain is completed
    , add that entry to the dictionary

iterate from 1 to 1000000

"""
n=1000000
dictionary = np.zeros(1000000)

for i in range (1,n):
    num = i
    count = 1
    while num > 1 :
           
        if num < i and num > 2 :          
            dictionary[i-1] =  count + int(dictionary[num-1] - 1)
            break
        count += 1   
        if num % 2 == 0:
            num = int(num/2)
        else:
            num = int(3*num + 1)
    if num == 1:
        dictionary[i-1] = count
    
    
print(dictionary[0:n])
print ( max(dictionary))
print ( np.argmax(dictionary)+1)
    
        
    
    
