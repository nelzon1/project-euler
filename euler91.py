# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 22:04:52 2018

@author: jaken
"""
import matplotlib.pyplot as plt
import pylab
import numpy
import sys
from matplotlib import interactive
interactive(True)
pylab.show()

gridMax = 50
precision = 12
xMax = gridMax+1
yMax = gridMax+1

#hl, = plt.plot([], [])
#plt.ion()
#plt.show()
#plt.axis([-0.5,gridMax,-0.5,gridMax])

def update_line(hl, a,b,c,colour):
    plt.cla()
   # hl.set_xdata([a[0],b[0],c[0]])
    #hl.set_ydata([a[1],b[1],c[1]])
    plt.axis([-0.5,gridMax,-0.5,gridMax])
    plt.plot([a[0],b[0]],[a[1],b[1]],colour,[b[0],c[0]],[b[1],c[1]],colour,[c[0],a[0]],[c[1],a[1]],colour)
    plt.pause(0.995)

def isRight2(a,b,c):
    x = b[0]**2 + b[1]**2
    y = c[0]**2 + c[1]**2
    z = (b[0]-c[0])**2 + (b[1] - c[1])**2
    
    if 0 in [x,y,z]:
        return False
    
    if x + y == z\
      or y + z == x\
      or z + x == y:
        return True
    
    return False



def isRight(a,b,c):
    
    if a==b or b==c or a==c:
        return False

    try:
        l1 = round((a[1] - b[1]) / (a[0] - b[0]),precision)
    except ZeroDivisionError:
        l1 = 'N'
        
    try:
        l2 = round((b[1] - c[1]) / (b[0] - c[0]),precision)
    except ZeroDivisionError:
        l2 = 'N'
        
    try:
        l3 = round((c[1] - a[1]) / (c[0] - a[0]),precision)
    except ZeroDivisionError:
        l3 = 'N'
  

    try:    
        if (round(-1 / l1,precision) == l2):
            return True  
    except (TypeError, ZeroDivisionError):
        if (l1 == 'N' and l2 == 0) or (l2 == 'N' and l1 == 0):
            return True
    try:    
        if (round(-1/l2,precision) == l3):
            return True  
    except (TypeError, ZeroDivisionError):
        if (l2 == 'N' and l3 == 0) or (l3 == 'N' and l2 == 0):
            return True
    try:    
        if (round(-1 / l1,precision) == l3):
            return True  
    except (TypeError, ZeroDivisionError):
       if (l1 == 'N' and l3 == 0) or (l3 == 'N' and l1 == 0):
            return True
        
    return False
    


triangles = set()

for x1 in range (0,xMax):
    for y1 in range(0,yMax):
        
        for x2 in range(0,xMax):
            for y2 in range(0,y1+1):
                
                if isRight2((0,0),(x1,y1),(x2,y2)):
                    #update_line(hl,(0,0),(x1,y1),(x2,y2),'g')
                    triangles.add( tuple( sorted( [tuple([x1,y1]),tuple([x2,y2])] ) ) )
                else:
                    t=1
                    #update_line(hl,(0,0),(x1,y1),(x2,y2),'r')
                    #read = input("Paused")
                  
print(len(triangles))
plt.show()
#read = input("Complete")