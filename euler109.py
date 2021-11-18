# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 14:36:06 2018

@author: JNelson
"""

'''
Euler109

Checking out in Darts

'''
def getValue( space ):  
    if space[0] == 'D':
        return int(space[1:]) * 2    
    elif space[0] == 'T':
        return int(space[1:]) * 3  
    else:
        return int(space)

spaces = [f(x) for x in range(1,21) for f in (lambda x: str(x), lambda x: 'D'+str(x),lambda x: 'T'+str(x))] + ['25','D25']

#Recursive function to return the possible ways of checking out at a certain value.
def throwDart(count,throws=[]):
    sols = set()
    if len(throws) == 2:
        possible = [x for x in spaces if getValue(x) == count and x[0]=='D']
        return [throws + [x] for x in possible]
    else:
        for i in spaces:
            if getValue(i) == count and i[0] == 'D':
                sols.add(tuple(sorted(throws) + [i]))
            elif getValue(i) >= count:
                continue
            else:
                tmpSol = throwDart(count-getValue(i),throws + [i])
                for sol in tmpSol:
                    if len(sol) > 1:
                        sol = sorted(sol[:-1]) + [sol[-1]]
                    sols.add(tuple(sol))            
    return sols

finalCount = 0
for i in range(1,100):
    finalCount += len(throwDart(i))
    
print(finalCount)