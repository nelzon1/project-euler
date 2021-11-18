# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 20:01:52 2017

@author: jaken
"""

def ctf_period(z):
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
        
    return alpha

print(ctf_period(14))
'''
biggest = [1,1,1]
for i in range(2,1001):
    if i**(1/2)%1==0:
        continue
    solution = pell(i)
    if solution[0]>biggest[0]:
        biggest=solution
print(biggest)
'''
count = 0
for i in range(2,10001):
    if int(i**(1/2))**2 == i:
        continue
    if len(ctf_period(i)[1:]) %2 == 1:
        count +=1
        
print(count)