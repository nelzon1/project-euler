# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 20:51:17 2017

@author: jaken
"""

import math as m

def chain_count(n):
    terms = [n]
    current_term = n
    while True:
        current_term = sum([m.factorial(int(x)) for x in str(current_term)])
        if current_term not in terms:
            terms.append(current_term)
        else:
            break
    return len(terms)
    
chain_count(169)
total=0
for i in range (1,1000000):
    if chain_count(i)==60:
        total+=1
        
print(total)