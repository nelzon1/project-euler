# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 12:58:40 2017

@author: jaken
"""

def nth_convergent(z,n):
    alpha = [z**(1/2)]
    if int(alpha[0])**2 == z:
        return alpha[0]
    
    for i in range(n):
        alpha.append(1/(alpha[-1]%1))
        
    frac = [int(alpha[-1]),1]
    
    for x in range(len(alpha[1:])):
        d=frac[0]
        frac[0]=frac[1]+int(alpha[-2-x])*frac[0]
        frac[1]=d
    frac.append((frac[0]/frac[1]))    
    return frac


nth_convergent(61,25)

solutions = []
for z in range (62,64):
    alpha = [z**(1/2)]
    if int(alpha[0])**2 == z:
        continue
    
    frac = nth_convergent(z,1)
    n = 2
    while (frac[0]**2 - z*frac[1]**2 != 1):
        frac = nth_convergent(z,n)
        n += 1  
    solutions.append((frac[0],frac[1],z))
















"""
stinkers = []
solutions = []
for d in range (2,1001):
    if d**(1/2) % 1 == 0:
        continue
    solved_outer = False
    x =2
    while not solved_outer:   
        solved_inner = False
        y = round(((x**2 - 1) / d)**(1/2))
        if x**2 - (d * (y)**2) == 1 and (y) != 0:
            solutions.append((int(x),int(d),int(y)))
            solved_outer = True
            break
        x+=1

        
largest = solutions[0]        
for s in solutions:
    if largest[0] < s[0]:
        largest = s
        
print(largest)
"""