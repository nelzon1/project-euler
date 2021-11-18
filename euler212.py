# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 19:29:03 2016

@author: jaken
"""

space_3d =  [ [ [0]*10400 ]*10400 ]*10400

def s(k):
    if k > 55:
        return s_56(k)
    else:
        return s_55(k)
    
def s_55 (k):
    return (100003 - 200003 * k + 300007 * k**3) % 1000000
    
def s_56 (k):
    return (s(k-24) + s(k-55)) % 1000000
    
def cuboid(n):
    x = s(6*n-5) % 10000
    y = s(6*n-4) % 10000
    z = s(6*n-3) % 10000
    dx = 1 + ( s(6*n-2) % 399)
    dy = 1 + ( s(6*n-1) % 399)
    dz = 1 + ( s(6*n) % 399)
    for xx in range(x,x+dx):
        for yy in range(y,y+dy):
            for zz in range(z,z+dz):
                space_3d[xx][yy][zz]=1
 
''' 
for n in range (1,2):
    cuboid(n)
    
#print (sum(map(sum,space_3d)))
volume = 0
for xx in space_3d:
    volume += sum ( sum (z) for z in xx)
'''