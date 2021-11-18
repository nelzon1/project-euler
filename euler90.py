# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 20:04:18 2018

@author: jaken
"""

import itertools as it

digits = [x for x in range(0,10)]

comb = it.combinations(digits,6)

count = 0
for i in comb:
    print(i)
    count+=1
    
print (count)

dice = []

winners = set()

for i in it.combinations(digits,6):
    if 6 in i and 9 in i:
        #do nothing
        e=1
    elif 9 in i:
        i = tuple([x for x in i] + [6])
    elif 6 in i:
        i = tuple([x for x in i] + [9])
        
    for j in it.combinations(digits,6):
        
        if 6 in j and 9 in j:
            #do nothing
            e=1
        elif 9 in j:
            j = tuple([x for x in j] + [6])
        elif 6 in j:
            j = tuple([x for x in j] + [9])
        squares = set()
        #start set of squares
        #add to it if combination is square
        
        for x in i:
            for y in j:
                if x == y:
                    continue
                
                num1 = str(x) + str(y)
                num2 = str(y) + str(x)
                if int(num1)**(1/2) % 1 == 0:
                    squares.add(num1)
                if int(num2)**(1/2) % 1 == 0:
                    squares.add(num2)
                    
        if len(squares) == 9:
            winners.add(tuple(sorted([i,j])))
        #check both directions of combinations
        
        #if set length is equal to 9
        #add tuple to list of dice combos
        
        dice.append((i,j))
        


