# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 12:01:59 2021

@author: jaken
"""

#Euler 719

import time

start = time.time()



def square_list(N):
    sqlist = [16]
    nextnum = 5
    while sqlist[-1] < N:
        sqlist.append(nextnum * nextnum)
        nextnum = nextnum + 1
    return sqlist

    
def maxLen(S):
    maxlen = 0
    if not S:
        return maxlen
    for s in S:
        if len(s) > maxlen:
            maxlen = len(s)
    return maxlen
    
def combos(s):
  if not s:
    return
  yield (s,)
  for i in range(1, len(s)):
    for c in combos(s[i:]):
      yield (s[:i],) + c

def checksq(N):
    root = int(N**(1/2))
    trials = list(combos(str(N)))
    for trial in trials:
        if maxLen(trial) < len(str(root)) - 1:
            continue
        if sum([int(x) for x in trial]) == root:
            return True
    return False

def checksqDEBUG(N):
    root = int(N**(1/2))
    trials = list(combos(str(N)))
    for trial in trials:
        if maxLen(trial) < len(str(root)) - 1:
            continue
        if sum([int(x) for x in trial]) == root:
            return trial
    return False

#for c in combos('Bang'):
#  print(c)

#comb = list(combos('1234567'))
#for combo in comb:
#    print(maxLen(combo),combo)

cnt = 0
ssum = 0
#for psquare in square_list(1000000000000):
#    if checksq(psquare):
#        cnt = cnt + 1
#        ssum = ssum + psquare


for psquare in square_list(10**12):
    test = checksqDEBUG(psquare)
    if test:
        print(psquare, int(psquare**(1/2)),maxLen(test), test)
'''

for psquare in square_list(200000000):
    for trial in combos(str(psquare)):
        if sum([int(x) for x in trial]) == int(psquare**(1/2)):
           cnt = cnt + 1
           ssum = ssum + psquare 
           break
       
'''

end = time.time()
print('time: ' + str(end - start))