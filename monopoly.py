# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 19:58:51 2017

@author: jaken
"""

import numpy as np
'''
from collections import Counter
#Create histograms for rolling pairs of dice, 6 sided and 4 sided
hist6 = sorted([(x,y) for x,y in dict(Counter([sum(x) for x in [(x,y) for x in range(1,7) for y in range(1,7)]])).items()],key = lambda x:x[1],reverse=True)
hist4 = sorted([(x,y) for x,y in dict(Counter([sum(x) for x in [(x,y) for x in range(1,5) for y in range(1,5)]])).items()],key = lambda x:x[1],reverse=True)
'''

roll4 = [(x,y) for x in range(1,5) for y in range(1,5)]
roll6 = [(x,y) for x in range(1,7) for y in range(1,7)]

def next_R(position):
    if position < 5 or position >= 36:
        position = 5
    elif 6 <= position and position < 15:
        position = 15
    elif 16 <= position and position < 25:
        position = 25
    elif 26 <= position and position < 35:
        position = 35
    return position

def next_U(position):
    if position < 12 or position >= 29:
        position = 12
    elif 13 <= position and position < 28:
        position = 28
    return position

def chance(position):
    possibilities = dict()
    possibilities['0'] = 1/16.0
    possibilities['10'] = 1/16.0
    possibilities['11'] = 1/16.0
    possibilities['24'] = 1/16.0
    possibilities['39'] = 1/16.0
    possibilities['5'] = 1/16.0
    possibilities[str((position-3) % 40 )] = 1/16.0
    possibilities[str(next_R(position))] = 2/16.0
    possibilities[str(next_U(position))] = 1/16.0
    possibilities[str(position)] = 6/16.0
    return possibilities
    
    
def comchest(position):
    possibilities = dict()
    possibilities['00'] = 1/16.0
    possibilities['10'] = 1/16.0
    possibilities[str(position)] = 14/16.0
    return possibilities


def if_special(position):
    if position in [2,17,33]:
        a=1
    elif position in [2,17,33]:
        a=1
    else:
        return position
    
    
markov = np.zeros([40,40])

#x = 0 is Go, x= 1 is A1. (x=0,y=0) is go -> go. (x=0,y=1) is go -> a1

for x in range(0,40):
    
        for roll in roll4:
            
            if (sum(roll) + x)%40 in [2,17,33]:
                poss = comchest((sum(roll) + x)%40)
                for square in poss:
                    markov[x][int(square)] += poss[square]
            elif (sum(roll) + x)%40 in [7,22,36]:
                poss = chance((sum(roll) + x)%40)
                for square in poss:
                    markov[x][int(square)] += poss[square]
            
                
            if roll[0] == roll[1]:
                
                for roll2 in roll4:
                    
                    if (sum(roll2) + sum(roll) + x)%40 in [2,17,33]:
                        poss = comchest((sum(roll2) + sum(roll) + x)%40)
                        for square in poss:
                            markov[x][int(square)] += poss[square]/4.0
                    elif (sum(roll2) + sum(roll) + x)%40 in [7,22,36]:
                        poss = chance((sum(roll2) + sum(roll) + x)%40)
                        for square in poss:
                            markov[x][int(square)] += poss[square]/4.0
                            
                    if roll2[0] == roll2[1]:
                        
                        for roll3 in roll4:
                            if roll3[0] == roll3[1]:
                                markov[x][10] += 1
                                continue
                            if (sum(roll3) + sum(roll2) + sum(roll) + x)%40 in [2,17,33]:
                                poss = comchest((sum(roll3) + sum(roll2) + sum(roll) + x)%40)
                                for square in poss:
                                    markov[x][int(square)] += poss[square]/16.0
                            elif (sum(roll3) + sum(roll2) + sum(roll) + x)%40 in [7,22,36]:
                                poss = chance((sum(roll3) + sum(roll2) + sum(roll) + x)%40)
                                for square in poss:
                                    markov[x][int(square)] += poss[square]/16.0
                                    


            markov[x][(x+sum(roll))%40] += 1
                
            
        



















