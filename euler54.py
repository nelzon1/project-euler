# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 21:06:21 2016

@author: jaken
"""
from time import clock
from collections import Counter

def getKey1(item):
    return item[1]
    
def getKey0(item):
    return item[0]

def is_flush(cards):
    if len(Counter(list(zip(*cards))[1]))==1:
        return 1
    return 0

def is_straight(cards):
    for x in range(1,len(cards)):
        if x == 1:
            if cards[0][0]==14 and cards[1][0]==5:
                continue
        if int(cards[x][0]) != int(cards[x-1][0]) - 1:
            return 0
    return 1    

def rank(cards):
    values = dict(Counter(list(zip(*cards))[0]))
    faces = [ (x,values[x]) for x in values ]
    faces.sort(key=getKey1,reverse=True)

    results = []
    
    if is_flush(cards) and is_straight(cards):
        results.append(ranks['straight flush'])
        results.append(cards[0][0])
        results.append(cards[1][0])
        
    elif max(values.values()) == 4:
        results.append(ranks['quads'])
        results.append(faces[0][0])
        
    elif max(values.values()) == 3 and min(values.values()) == 2:
        results.append(ranks['full house'])
        results.append(faces[0][0])
        results.append(faces[1][0])

    elif is_flush(cards):
        results.append(ranks['flush'])
        results.extend(list(zip(*cards))[0])

    elif is_straight(cards):
        results.append(ranks['straight'])
        results.append(cards[0][0])
        results.append(cards[1][0])

    elif max(values.values()) == 3:
        results.append(ranks['triple'])
        results.append(faces[0][0])
        faces=faces[1:]
        faces.sort(reverse=True)
        results.extend((list(zip(*faces))[0]))
        
    elif max(values.values()) == 2 and len(values) == 3:    
        results.append(ranks['two pair'])
        results.append(max([faces[0][0],faces[1][0]]))
        results.append(min([faces[0][0],faces[1][0]]))
        results.append(faces[2][0])
        
    elif max(values.values()) == 2:
        results.append(ranks['pair'])
        results.append(faces[0][0])
        faces=faces[1:]
        faces.sort(reverse=True)
        results.extend((list(zip(*faces))[0]))

    else:
        results.append(ranks['high card'])
        results.extend(list(zip(*cards))[0])

    return results


ranks = {'high card':0,'pair':1,'two pair':2, 'triple':3, 'straight':4,'flush':5,\
        'full house':6, 'quad':7, 'straight flush':8}

start_time = clock()      
data = open('euler54.txt','r')




p1 = []
p2 = []
def next_game():
    p1[:]=[]
    game = data.readline()
    game=game[:-1]
    game=str(game)
    game = game.replace('T','10')
    game = game.replace('J','11')
    game = game.replace('Q','12')
    game = game.replace('K','13')
    game = game.replace('A','14')
    pp=game.split()
    for card in pp:
        if len(card)==3:
            p1.append((int(card[:2]),card[2]))
        else:
            p1.append((int(card[0]),card[1]))

      
wincount = 0
for i in range (0,1000):
    next_game()
    p2=p1[5:]
    p1=p1[:5] 
    p1.sort(reverse=True)
    p2.sort(reverse=True)
    player1 = rank(p1)
    player2 = rank(p2)
    for r1,r2 in zip(player1,player2):
        if r1 > r2:
            wincount += 1
            break
        elif r1 < r2:
            break
       
print (wincount)
print ("Took", clock() - start_time, "seconds")
   


