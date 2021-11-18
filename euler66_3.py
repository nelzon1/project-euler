# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 21:06:31 2017

@author: jaken
"""

def pell(z):
    if int(z**(1/2))**2 == z:
        return 'no solution ' + str(z) +' is a perfect square'
    alpha = [int(z**(1/2))]
    c1=1
    b1=0
    while alpha[-1] != 2*alpha[0] or len(alpha)==0: 
        b2 = c1*(alpha[-1]*c1 - b1)
        c2 = z - (b1 - alpha[-1]*c1)**2  
        b1=b2//c1
        c1=c2//c1
        alpha.append( (int(z**(1/2)) + b1 ) // c1 )
        
    frac = [int(alpha[-2]),1]
    if frac[0]**2 - z*frac[1]**2 == 1:
        return frac
    for x in range(len(alpha[1:])-1):
        d=frac[0]
        frac[0]=frac[1]+int(alpha[-3-x])*frac[0]
        frac[1]=d
        
    if frac[0]**2 - z*frac[1]**2 != 1:
        alpha.extend(alpha[1:])
        frac = [int(alpha[-2]),1]
        for x in range(len(alpha[1:])-1):           
            d=frac[0]
            frac[0]=frac[1]+int(alpha[-3-x])*frac[0]
            frac[1]=d
            
    frac.append(z)    
    return frac

print(pell(14))

biggest = [1,1,1]
for i in range(2,1001):
    if i**(1/2)%1==0:
        continue
    solution = pell(i)
    if solution[0]>biggest[0]:
        biggest=solution
print(biggest)
    
    
'''
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
    '''