# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 20:47:21 2018

@author: jaken
"""
import math
import decimal as dec
import string
import time
start = time.clock()
def newton(a,b):
    #a is the current guess
    #b is the number we're rooting
    #b = dec.Decimal(a)
    return a - (((a * a) - b) /(2 * a) )

dec.getcontext().prec = 120

def root(a):
    if math.sqrt(a) % 1 == 0:
        return math.sqrt(a)
    #x0 = dec.Decimal(round(math.sqrt(a),2))
    x0 = dec.Decimal(1.3)
    x1 = dec.Decimal(a)
    a = dec.Decimal(a)
    same = False
    count = 0
    while not same:
        count+=1
        x1 = newton(x0,a)
        if str(x1)[:115] == str(x0)[:115] :
            #print(count)
            break
        x0 = x1
    return x0

total = 0
for i in range(1,1001):
    if math.sqrt(i) % 1 == 0:
        continue
    for digit in str(root(i)).replace('.','')[:100]:
        total+=int(digit)
print(total)
print((time.clock() - start))