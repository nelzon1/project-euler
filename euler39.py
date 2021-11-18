# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 12:47:26 2016

@author: jaken
"""
import math as m
num_solutions = [0]
def pythagoras(perimeter):
    solutions = 0
    for a in range(1,int(perimeter/2)):
        for b in range (1,int(perimeter/2)):
            if (perimeter == a + b + m.sqrt(a*a + b*b)):
                solutions+=1
    return int(solutions/2)

#num_solutions.append(solutions)

print(pythagoras(120))
maximum=0
num_sol =0
for i in range(1,1001):
    if pythagoras(i) > num_sol:
        maximum=i
        num_sol = pythagoras(i)
        
print(maximum)
print(num_sol)