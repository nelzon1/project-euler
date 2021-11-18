# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 16:04:21 2018

@author: jaken
"""

#perimeter total
#loop over recurrence
#check each solution set
#add perimeter if needed
#
#print total


perimeter = 0

x = 1
y = 0

LIMIT = 10**9

while True:
    temp = x
    x = 2*x + 3*y
    y = temp + 2*y
    
    a= (2 * x - 1)/3
    b= a - 1
    #case 2 :  b = a - 1
    tripleA = (2 * x - 1)
    tripleArea = (x - 2) * y
    if tripleA > LIMIT:
        break

    #check if a is an integer
    if tripleA % 3 == 0 and tripleArea % 3 == 0 and tripleA > 0 and tripleArea > 0:
        perimeter += (tripleA - 1)
    
    a= (2 * x + 1)/3
    b= a + 1
    #case 1 :  b = a + 1
    #check if a is an integer
    tripleA = (2 * x + 1)
    tripleArea = (x + 2) * y
    
    if tripleA % 3 == 0 and tripleArea % 3 == 0 and tripleA > 0 and tripleArea > 0:
        perimeter += tripleA + 1
    
    
print(perimeter)