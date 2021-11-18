# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 13:53:07 2018

@author: jaken
"""

import itertools as it

def all_subsets(ss):
    return it.chain(*map(lambda x: it.combinations(ss, x), range(1, len(ss)+1)))


DIGITS = ('1','2','3','4','5','6','7','8','9')
OPERATORS = ('+','-','*','/')
BRACKETS = ('LR--','L-R-','-LR-','-L-R','--LR','LRLR','ARR-','-ARR','LLB-','-LLB')


digitSets  = list(it.combinations(DIGITS,4))
operatorSets  = list(set(sum([list(it.permutations(x)) for x in it.combinations_with_replacement(OPERATORS,3)],[])))
bracketSets  = BRACKETS


allAnswers = []
candidates = []

for digitSet in digitSets:
    
    answers = set()
    
    for digitOrder in it.permutations(digitSet,4):
    
        for operatorSet in operatorSets:
            
            for bracket in bracketSets:
                 
                #initialize string for mathematical sentence
                operation = ''
                
                #first bracket
                if bracket[0] == 'L':
                    operation += '( '
                elif bracket[0] == 'A':
                    operation += '( ( '
                    
                #first digit and operator
                operation += digitOrder[0] + ' ' + operatorSet[0] +  ' '
                
                #second bracket position, left of digit
                if bracket[1] == 'L':
                    operation += '( '
                elif bracket[1] == 'A':
                    operation += '( ( '
                    
                #second digit
                operation += digitOrder[1] + ' '
                
                #second brack position, right of digit
                if bracket[1] == 'R':
                    operation += ') '

                #second operator
                operation += operatorSet[1] + ' '
                
                #third bracket position, left of digit
                if bracket[2] == 'L':
                    operation += '( '

                #third digit
                operation += digitOrder[2] + ' '
                
                #third brack position, right of digit
                if bracket[2] == 'R':
                    operation += ') '
                elif bracket[2] == 'B':
                    operation += ') ) '
                #second operator
                operation += operatorSet[2] + ' '
                
                #fourth digit
                operation += digitOrder[3] + ' '
                
                #fourth brack position, right of digit
                if bracket[3] == 'R':
                    operation += ')'
                elif bracket[3] == 'B':
                    operation += ') )'

                try:
                    # print(operation, ' = ', eval(operation))
                    answers.add(eval(operation))
                except ZeroDivisionError:
                    None
                    
    tempList = [int(x) for x in sorted(list(answers)) if x % 1 == 0 and x > 0]
    longestChain = 1
    curChain = 1
    try:
        lastAnswer = tempList[0]
        for answer in tempList[1:]:
            if answer == lastAnswer + 1:
                curChain += 1
                if curChain > longestChain:
                    longestChain = curChain
            else:
                curChain = 1
            lastAnswer = answer
    except IndexError:
        longestChain = 0

            
        
    candidates.append((digitSet,longestChain))
    #print ("Digit set done: ", digitSet, "\nLongest chain: ", longestChain)

ans1 = 0
ans2 = []
for x in candidates:
    if x[1] > ans1:
        ans1 = x[1]
        ans2 = x[0]
print("The largest chain is " + str(ans1) + ", and is formed by these digits: ", ans2)