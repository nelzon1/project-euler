# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 00:12:54 2017

@author: jaken
"""
from collections import Counter

def triangle(n):    
    return int(n*(n+1) / 2)

def square(n):   
    return int(n*n)

def pentagonal(n):   
    return int(n*(3*n-1) / 2)

def hexagonal(n):   
    return int(n*(2*n - 1))

def heptagonal(n):   
    return int(n*(5*n - 3) / 2)

def octagonal(n):   
    return int(n*(3*n-2))

n = 5000
        
     
matrix = [[],[],[],[],[],[]]

for z in range(n+1):
    if len(str(triangle(z))) == 4 and str(triangle(z))[2]!='0':
        matrix[0].append(triangle(z))
    if len(str(square(z))) == 4 and str(square(z))[2]!='0':
        matrix[1].append(square(z))
    if len(str(pentagonal(z))) == 4 and str(pentagonal(z))[2]!='0':
        matrix[2].append(pentagonal(z))
    if len(str(hexagonal(z))) == 4 and str(hexagonal(z))[2]!='0':
        matrix[3].append(hexagonal(z))
    if len(str(heptagonal(z))) == 4 and str(heptagonal(z))[2]!='0':
        matrix[4].append(heptagonal(z))
    if len(str(octagonal(z))) == 4 and str(octagonal(z))[2]!='0':
        matrix[5].append(octagonal(z))
    if len(str(triangle(z))) > 4:
        break


'''
for kind in matrix: 
    for s in kind:
        
        for 
        if str(t)[2:] == str(s)[:2]:
            forwards = True                 
            
'''


partial_2 = set()
for j in range(6):
    for i in range(6):
        if i == j:
            continue
        for y in matrix[i]:
            for x in matrix[j]:
               if str(x)[2:] == str(y)[:2]:
                   #print(x,y)
                   partial_2.add(((x,j),(y,i),int( str(min([x,y])) + str(max([x,y])) )))

print(len(partial_2))

partial_4=set()
leftover_2 = set(partial_2)
for x in partial_2:
    for y in partial_2:
        if x == y:
            continue
        dupes = False
        count = Counter([x[0][1],x[1][1],y[0][1],y[1][1] ])           
        for z in count:
            if count[z] > 1:
                dupes = True
        if str(y[1][0])[2:] == str(x[0][0])[:2] and not dupes:
                   #print(x,y)
            z=[ i for i in y]
            z.extend(x)
            z=tuple(z)
            partial_4.add(z)
            #leftover_2.discard(x)
            #leftover_2.discard(y)            
            
            
print(len(partial_4))     
print(len(leftover_2))          
             
partial_6=set()               
for i in partial_4:
    for j in leftover_2:
        
        dupes = False
        count = Counter([i[0][1],i[1][1],i[3][1],i[4][1],j[0][1],j[1][1] ])           
        for z in count:
            if count[z] > 1:
                dupes = True
        if str(i[4][0])[2:] == str(j[0][0])[:2] and not dupes and str(i[0][0])[:2] == str(j[1][0])[2:]:
                   #print(x,y)
            z=[ k for k in i]
            z.extend(j)
            z=tuple(z)
            partial_6.add(z)
answer = list(partial_6)
print(sum([2512,1281,8128,2882,8256,5625]))
print([2512,1281,8128,2882,8256,5625])             
               
               
               
               
               
               