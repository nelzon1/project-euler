# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 20:00:01 2018

@author: jaken
"""

#function to calculate domain and slope
#once we get the results, look for 0 appearing in 2 domains
#for those given domains:
#    calculate the y intercepts
#    see if they span 0
#    add one to count if it does
#    

triangles= []

with open('euler102.txt','r') as data:
    triangles = [list(map( lambda x: int(x),triangle.split(','))) for triangle in data.read().splitlines()]

print("Triangles impored from euler102.txt successfully.")

def line(A,B):
    domain = tuple(sorted([A[0],B[0]]))
    
    try:
        slope = ( B[1] - A[1] ) / (B[0] - A[0])
    except ZeroDivisionError:
        slope = 9999999     
        
    try:     
        intercept = slope * -1 * A[0] + A[1]
    except ZeroDivisionError:
        intercept = slope * -1 * B[0] + B[1]
        
    return domain, slope, intercept


#print (triangles)
    
total = 0

for triangle in triangles:
    a = triangle[0:2]
    b = triangle[2:4]
    c = triangle[4:6]
    
    ab = line(a,b)
    bc = line(b,c)
    ca = line(c,a)
    
    candidates = []
    
    for segment in [ab,bc,ca]:
        #if 0 is in the domain, store the intercept in a list for sorting
        if segment[0][0] <= 0 and segment[0][1] >= 0:
            candidates.append(segment[2])
    candidates = sorted(candidates)
    if len(candidates) >= 1:
        if candidates[0] <= 0 and candidates[1] >= 0:
            total += 1
            print ("origin contained: \n\tA: ", a, "\n\tB: ", b, "\n\tC: ", c)
        elif candidates[0] == 0:
            total += 1
            print ("origin contained: \n\tA: ", a, "\n\tB: ", b, "\n\tC: ", c)
            
print("Number of triangles containing the origin: ", total)