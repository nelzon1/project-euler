# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 12:50:49 2016

@author: jaken
"""
import numpy as np
import matplotlib.pyplot as plt



import math
def digit_pow(x,y):
    str_x = str(int(x))
    sum_x = 0
    for i in str_x:
        sum_x += math.pow(int(i),y)
    return sum_x
    
x=np.zeros(100000)
y=np.zeros(100000)
answers=[]
for i in range (0,100000):
    x[i]=i
    y[i]=digit_pow(i,2)
    if y[i]==x[i]:
        answers.append(x[i])
    
answers.remove(1)
answers.remove(0)

print(answers)
print(sum(answers))
plt.plot(x,y,'ro')
#plt.plot(x,x, 'b:')
plt.show()

