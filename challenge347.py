# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 22:35:33 2018

@author: jaken
"""

'''
Challenge 347

Detecting and counting hours

There is a light in a room which lights up only when someone is in the room (think motion detector). You are given a set of intervals in entrance and exit times as single integers, and expected to find how long the light has been on. When the times overlap, you need to find the time between the smallest and the biggest numbers in that interval.
Input Description

You'll be given a set of two integers per line telling you the time points that someone entered and exited the room, respectively. Each line is a visitor, each block is a room. Example:

1 3
2 3
4 5

Output Description

Your program should report the number of hours the lights would be on. From the above example:

3
'''

def overlap(a,b):
    if int(a[0]) <= int(b[1]) and int(b[0]) <= int(a[1]):
        return True
    return False

        
def consolidate(times):
    if len(times) == 0:
        return 0
    count = 0
    for x in times:
        
        for y in times[times.index(x)+1:]:
            if overlap(x,y):
                z = tuple([min([x[0],y[0]]),max([x[1],y[1]])])
                times[times.index(x)] = z
                x = z
                count+=1
                times.pop(times.index(y))
    return count
            
        
with open('347.txt','r') as file:
    z = file.readlines()
    jobs = [tuple(y.split()) for y in z]


seed = consolidate(jobs)
while seed != 0:
    seed = consolidate(jobs)
    print( seed)
print('Consolidation Complete')
hours = 0
for x in jobs:
    hours += (int(x[1]) - int(x[0]))
print('Total hours: ' + str(hours) + '.')