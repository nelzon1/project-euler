# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 09:37:34 2017

@author: jaken
"""

class node:
    def __init__(self,val,dist):
        self.value=val
        self.distance=dist
        self.previous=0
        self.visited=False

def next_node(grid):
    low = 10000000
    for x in range(len(grid)):
        for y in range(len(grid)):
            if grid[x][y].distance < low and not grid[x][y].visited:
                address = (x,y)
                low = grid[x][y].distance
    if low == 10000000:
        return None
    return address
        
matrix = []
with open('euler83.txt','r') as data:
    for line in data.readlines():
        matrix.append([int(y) for y in line.split(",")])
  
grid = [[None for _ in range(80)] for _ in range(80)]

for i in range(len(matrix)):
    for j in range(len(matrix)):
        grid[i][j] = node(matrix[i][j],10000000)

total = grid[0][0].value
grid[0][0].distance=grid[0][0].value
        
if grid[0][0].distance + grid[0][1].value < grid[0][1].distance:
    grid[0][1].distance = grid[0][0].distance + grid[0][1].value
    grid[0][1].previous = (0,0)

if grid[0][0].distance + grid[1][0].value < grid[1][0].distance:
    grid[1][0].distance = grid[0][0].distance + grid[1][0].value
    grid[1][0].previous = (0,0)
grid[0][0].visited=True

nextaddy = next_node(grid)
while nextaddy != None:
    x_ind = nextaddy[0]
    y_ind = nextaddy[1]
    #right
    try:
        if grid[x_ind][y_ind].distance + grid[x_ind][y_ind+1].value < grid[x_ind][y_ind+1].distance and not grid[x_ind][y_ind+1].visited:
            grid[x_ind][y_ind+1].distance = grid[x_ind][y_ind].distance + grid[x_ind][y_ind+1].value
            grid[x_ind][y_ind+1].previous = (x_ind,y_ind)
    except IndexError:
        temp=1
    #down
    try:                
        if grid[x_ind][y_ind].distance + grid[x_ind+1][y_ind].value < grid[x_ind+1][y_ind].distance and not grid[x_ind+1][y_ind].visited:
            grid[x_ind+1][y_ind].distance = grid[x_ind][y_ind].distance + grid[x_ind+1][y_ind].value
            grid[x_ind+1][y_ind].previous = (x_ind,y_ind)
    except IndexError:
        temp=1
    #left
    if y_ind !=0:                
        if grid[x_ind][y_ind].distance + grid[x_ind][y_ind-1].value < grid[x_ind][y_ind-1].distance and not grid[x_ind][y_ind-1].visited:
            grid[x_ind][y_ind-1].distance = grid[x_ind][y_ind].distance + grid[x_ind][y_ind-1].value
            grid[x_ind][y_ind-1].previous = (x_ind,y_ind)
    
    #up
    if x_ind !=0:                  
        if grid[x_ind][y_ind].distance + grid[x_ind-1][y_ind].value < grid[x_ind-1][y_ind].distance and not grid[x_ind-1][y_ind].visited:
            grid[x_ind-1][y_ind].distance = grid[x_ind][y_ind].distance + grid[x_ind-1][y_ind].value
            grid[x_ind-1][y_ind].previous = (x_ind,y_ind)

        
    grid[x_ind][y_ind].visited=True
    nextaddy=next_node(grid)

print(grid[79][79].distance)
