# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 22:01:47 2017

@author: jaken
"""

''' 
Euler 62:
1. Loop through cubes to build sets of histograms depending on the total number of digits
2. For each set, see if any histogram is duplicated 5 times
3. Print results
'''
from collections import Counter
import time

def cubes(n):
    num = 1
    while num < n:
        yield num**3
        num+=1
 
current_len = 0      
repository = []
lexicon = {}

start = time.clock()
for cube in cubes(1000000):
    if len(str(cube)) > current_len:
        current_len +=1
        
        '''
        code to loop through the set of dictionaries in repository[-1]
        
        '''
        if len(repository) != 0:
            
            for hist in repository[-1]:
                ans = [hist]
                count = 0
                for test in repository[-1]:
                    if test == hist:
                        count+=1
                        ans.append(test)
                if count == 5:
                    
                    print(lexicon[hist],hist)
                    print ('-'*10, str(time.clock() - start) + ' s')
                    break
        repository.append([])
        
    current_dict = Counter(str(cube)).most_common()
    current_dict.sort()
    current_dict=tuple( (int(x),y) for x,y in current_dict)
    if current_dict not in lexicon:
        lexicon[current_dict] = cube
    repository[-1].append(current_dict)
    