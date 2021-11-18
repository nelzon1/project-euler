# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 18:29:44 2017

@author: jaken
"""
import math as m

def isprime(num):
    if num < 2:
        return 0
    for i in range(2,int(m.sqrt(num))+1):
        if num%i==0:
            return 0
    return 1     
    
def next_diag( term ):
    if term[0]==1:
        return (2,3)
    return (term[0]+1,term[1] + 2 * m.ceil((term[0] )/4) )
    
def square_fill(square):
    direction = 0
    x = int(len(square) /2)
    y=x
    notFinished=True
    count = 1
    position = 0
    line = 0
    while(notFinished):
        square[y][x]=count
        if (y == int(len(square))-1 ) and ( x == y ):
            break
        
        if position == line:
            if direction %2 ==0:
                line +=1
                
            direction+=1
            position = 0
            
        if direction % 4 == 0:
            y+=1 
        elif direction % 4 == 1:
            x+=1   
        elif direction % 4 == 2:
            y-=1    
        elif direction % 4 == 3:
            x-=1
        position += 1
        count += 1
    return square
n =7
diagonals = []
mysquare=[list(range(n)) for x in range(n)]
square = square_fill(mysquare)
#for x in mysquare:
 #   print (' '.join(str(x)))
count = 0   
primecount=0
for i in range(len(mysquare)):
    for j in range(len(mysquare)):
        if (i == j) or (i + j == n-1) :
            count +=1
            diagonals.append(mysquare[i][j])
            if isprime(mysquare[i][j]):
                primecount += 1
                
print (primecount)
print (count)
print ( primecount / count * 100)                
diagonals.sort()
print(diagonals)              
                
