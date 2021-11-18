# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 18:51:31 2021

@author: jaken
"""
import time

start = time.time()

cnt = 0
N= 10**6
searchstr='123'
D1 = 1.0043362776618689222137263
D2 = 9.946464728195732843107644962936416802
D3 = 9.989595361011175140421111135338132178395514
curVal = 1.237940039285380274899124224 # 2**90
curPow = 90
count = 1
while count < 678910:
    #the three differences Ive seen are: 196, 289, 485 (485 = 196 + 289)
    # 
    #try 196
    if curVal > 10:
        curVal = curVal / 10.0
    TVal = curVal * D1
    curPow = curPow + 196
    if str(TVal * 100)[:3] == searchstr:
        #print(str(curVal)[:5])
        count = count + 1
        curVal = TVal
        continue
    #try 289
    TVal = curVal * D2
    curPow = curPow + 93
    if str(TVal * 100)[:3] == searchstr:
        #print(str(curVal)[:5])
        count = count + 1
        curVal = TVal
        continue
        
    TVal = curVal * D3
    curPow = curPow + 196
    if str(TVal * 100)[:3] == searchstr:
        #print(str(curVal)[:5])
        count = count + 1
        curVal = TVal
        continue    
    print('Got stuck at ' + str(count))
    break
    

end = time.time()
print('time: ' + str(end - start))
print('Count: ' + str(count))
print('Current Power: ' + str(curPow))