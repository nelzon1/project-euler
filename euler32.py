# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 23:23:46 2016

@author: jaken
"""
import math as m

def pro_factor(n):
    factors = [1,n]
    for i in range (2,int(m.sqrt(n)) + 1):
        if n % i == 0:
            factors.append(i)
            if int(n/i) != i:
                factors.append(int(n/i))
    factors.sort()            
    return factors
    
    
#go through numbers, check if they have repeat digits
    #factor them and see if the factor pair makes a full 1-9 set with the product
    
def nodupes(num):
    dupe = []
    for digit in str(num):
        if (digit in dupe):
            return 0
        dupe.append(digit)
    return 1
    
panproducts = []
factorA = []
factorB = []
for i in range (1,10000):
    digits = []
    if not nodupes(i):
        continue
    for digit in str(i):
        if (digit == '0'):
            break
        digits.append(digit)
    else:    
        factors = pro_factor(i)
        if (len(factors) % 2 == 1):
            continue
        for x in range (1,int(len(factors)/2)):
            fdigits=[]
            for digit in str(factors[x]):
                if (digit in digits or digit in fdigits or digit == '0'):
                    break
                fdigits.append(digit)
            else:
                for digit in str(factors[len(factors)-x-1]):
                    if (digit in digits or digit in fdigits or digit == '0'):
                        break
                    fdigits.append(digit)
                else:
                    if (len(digits) + len (fdigits)==9):
                        panproducts.append(i)
                        factorA.append(factors[x])
                        factorB.append(factors[len(factors)-x-1])
                        break
print(sum(panproducts))
            
            
