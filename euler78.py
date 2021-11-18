# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 15:21:36 2017

@author: JNELSON
"""

def penta_gen(n):
    i=1
    while 0.5*i*(3*i-1) <= n :
        yield int(0.5*i*(3*i-1))        
        
        if i>0:
            i*=(-1)
        else:
            i = i*(-1) + 1
        
        
        
#for z in penta_gen(5):
#    print(z)
        
for z in penta_gen(5):
    print(z)        
partition = [1]
'''
for i in range(1,10):
    part = 0
    cycler = 0
    for z in penta_gen(i):
        if cycler % 4 < 2:
            part += partition[-1*z]
        else:
            part -= partition[-1*z]
        cycler+=1
    partition.append(part)
'''
i=1
while partition[-1] % 1000000 != 0:
#for g in range(101):
    part = 0
    cycler = 0
    for z in penta_gen(i):
        if cycler % 4 < 2:
            part += partition[-1*z]
        else:
            part -= partition[-1*z]
        cycler+=1
    partition.append(part)
    i+=1
 
print(i,partition[-1])
   
for g in partition:
    print(g,partition.index(g))