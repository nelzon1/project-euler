# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 23:44:20 2017

@author: jaken
"""

def triangle(z):   
    for n in range(z+1):
        yield int(n*(n+1) / 2)

def square(z):   
    for n in range(z+1):
        yield int(n*n)

def pentagonal(z):   
    for n in range(z+1):
        yield int(n*(3*n-1) / 2)

def hexagonal(z):   
    for n in range(z+1):
        yield int(n*(2*n - 1))

def heptagonal(z):   
    for n in range(z+1):
        yield int(n*(5*n - 3) / 2)

def octagonal(z):   
    for n in range(z+1):
        yield int(n*(3*n-2))

n = 500
        
tri_g, sq_g, pent_g, hexa_g, hept_g, octa_g = triangle(n),square(n),pentagonal(n),hexagonal(n),heptagonal(n),octagonal(n)       
        
tri, sq, pent, hexa, hept, octa = [],[],[],[],[],[]

for z in tri_g:
    l = len(str(z)) 
    if l < 4:
        continue
    elif l == 4 and str(z)[2]!='0':
        tri.append(z)
        continue
    elif l > 4:
        break
    
for z in sq_g:
    l = len(str(z)) 
    if l < 4:
        continue
    elif l == 4 and str(z)[2]!='0':
        sq.append(z)
        continue
    elif l > 4:
        break

for z in pent_g:
    l = len(str(z)) 
    if l < 4:
        continue
    elif l == 4 and str(z)[2]!='0':
        pent.append(z)
        continue
    elif l > 4:
        break

for z in hexa_g:
    l = len(str(z)) 
    if l < 4:
        continue
    elif l == 4 and str(z)[2]!='0':
        hexa.append(z)
        continue
    elif l > 4:
        break

for z in hept_g:
    l = len(str(z)) 
    if l < 4:
        continue
    elif l == 4 and str(z)[2]!='0':
        hept.append(z)
        continue
    elif l > 4:
        break

for z in octa_g:
    l = len(str(z)) 
    if l < 4:
        continue
    elif l == 4 and str(z)[2]!='0':
        octa.append(z)
        continue
    elif l > 4:
        break


for t in tri:
    
    for s in sq:
        if str(t)[2:] == str(s)[:2]:
            forwards = True                 
        
        for p in pent:
            
            for h in hexa:
                
                for hep in hept:
                            
                    
                    for o in octa:
                        
                        



























