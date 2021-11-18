# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 23:23:46 2016

@author: jaken
"""
    
    
#go through numbers, check if they have repeat digits
    #factor them and see if the factor pair makes a full 1-9 set with the product
import math as m
def nodupes(num):
    dupe = []
    for digit in str(num):
        if (digit in dupe):
            return 0
        dupe.append(digit)
    return 1
index = []
solutions=[]     
panmultiples = []   
for i in range (1,10000):
    digits = []
    for digit in str(i):
        if (digit == '0'):
            break
    else:    
        for x in range(1,10-int(m.log(i,10))):
            breaker=False
            for digit in (str(x*i)):
               if (digit in digits or digit == '0'):
                   breaker=True    
                   break 
               else:
                   digits.append(digit)    
            else:
               if (len(digits) == 9 ):
                   panmultiples.append(''.join(digits))
                   solutions.append(i)
                   index.append(x)
                   break
            if breaker:
                break
   

windex = panmultiples.index(max(panmultiples))        
#print(panmultiples)         
#print(solutions)   
print(max(panmultiples))           
print(solutions[windex])       
print(index[windex]) 
            
print(panmultiples)         
print(solutions)   
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
