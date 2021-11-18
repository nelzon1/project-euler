# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 20:00:10 2018

@author: jaken
"""

data = []
coefficients = []
import numpy as np


def gen(n):
    return 1 - n + n**2 - n**3 + n**4 - n**5 + n**6 - n**7 + n**8 - n**9 + n**10

for i in range(1,20):
    #print(i,gen(i))
    data.append([i,gen(i)])
    
for x in range (2,15):
    row = []
    for n in range (0,11):
        row.append((-1)**n * x**n)
    coefficients.append(row)

def subMatrix(n):
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(coefficients[i][j])
        row.append(data[i][1])
        matrix.append(row)
    return np.matrix(matrix)

def gaussian(n):
    mat = subMatrix(n)
    matrix = mat[:n,:n]
    solns = mat[:,n]
    return np.linalg.solve(matrix,solns)

def substitute(vector,j):
    coeff = coefficients[j][:len(vector)]
    sumz = 0
    for i in range(len(vector)):
        sumz += vector[i] * coeff[i]
    return sumz[0][0]

total = 0
for i in range(1,11):
    total += substitute(gaussian(i),i)[0,0]

print (total)