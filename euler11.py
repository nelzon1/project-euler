# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 21:56:23 2016

@author: jaken
"""

import numpy as np

def multiply(i,j,matrix):
    products = []
    if j < 17:
        products.append(matrix[i,j] * matrix[i,j+1] * matrix[i,j+2] * matrix[i,j+3])
        products.append(matrix[i,j] * matrix[i-1,j+1] * matrix[i-2,j+2] * matrix[i-3,j+3])
        if i < 17:
            products.append(matrix[i,j] * matrix[i+1,j+1] * matrix[i+2,j+2] * matrix[i+3,j+3])
            
    if j > 2:
        products.append(matrix[i,j] * matrix[i,j-1] * matrix[i,j-2] * matrix[i,j-3])
        products.append(matrix[i,j] * matrix[i-1,j-1] * matrix[i-2,j-2] * matrix[i-3,j-3])
        if i < 17:
            products.append(matrix[i,j] * matrix[i+1,j-1] * matrix[i+2,j-2] * matrix[i+3,j-3]  )  
    
    
    if i > 2:
        products.append(matrix[i,j] * matrix[i-1,j] * matrix[i-2,j] * matrix[i-3,j])
    if i < 17:    
        products.append(matrix[i,j] * matrix[i+1,j] * matrix[i+2,j] * matrix[i+3,j])
        
    return max(products)

x = np.loadtxt('euler11.txt',delimiter='\t')
maxproduct = 1
a= np.zeros((20,20))
for i in range(0,20):
    for j in range (0,20):
        a[i,j]=multiply(i,j,x)


print (np.amax(a))
