# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 20:42:33 2016

@author: jaken
"""
"""
#Recusive Trianlge

read triangle into matrix
duplicate it to the pathsum matrix

int pathsum(row,column):

number = triangle(row,col)
If top row: element = number

if edge: element = number + row-1 edge number

if middle: element = number + max(pathsum(row-1,col),pathsum(row,col))
pathsum_matrix = element
return element
"""
import copy

data = open('euler12.txt','r')
#global triangle
triangle = []
solutions = []
str = ' '
i=0
while str != '':
    str = data.readline()
    #global triangle
    triangle.append([int(s) for s in str.split() if s.isdigit()])
    i += 1
#global solutions
triangle.pop()
solutions = copy.deepcopy(triangle)
iterate = copy.deepcopy(triangle)


def pathsum(row,col):
    num = triangle[row][col]
    if row == 0:
        return num
    elif col == 0:
        #global solutions
        solutions[row][col] = num + pathsum(row-1,col)
    elif col == len(triangle[row])-1:
        #global solutions
        solutions[row][col] = num + pathsum(row-1,col-1)
    else:
        #global solutions
        solutions[row][col] = num + max([ pathsum(row-1,col) , pathsum(row-1,col-1) ] )
    return solutions[row][col]

"""
for i in range (0,len(triangle)):
    pathsum(len(triangle)-1,i)

n=len(triangle)
for i in range (0,n):
    pathsum(n-1,i)
print (pathsum(0,0) )

print( max(solutions[n-1]) )

"""

for row in range(1,len(triangle)):
    for col in range (0,len(triangle[row])):
        num = triangle[row][col]
        if col == 0:
            iterate[row][col] = num + iterate[row-1][col]
        elif col == len(triangle[row])-1:
            iterate[row][col] = num + iterate[row-1][col-1]
        else:
            iterate[row][col] = num + max([ iterate[row-1][col] , iterate[row-1][col-1] ] )
