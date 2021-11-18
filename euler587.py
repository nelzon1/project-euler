# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 00:38:09 2017

@author: jaken
"""

import math as m
NUM_INTERVALS = 1000
#write b
BASE_AREA = 0.25 * (1 - (m.pi / 4) )
# write b'

# write 
# write Newton's Method
def circle(x):
    return 0.5 - m.sqrt(0.25-(x-0.5)**2)

def b(x,n):
    return circle(x) - (x/n) 
    
def b_prime(x,n):
    return (x-0.5)/m.sqrt(0.25-(x-0.5)**2) -(1/n)
    
def area(x,n):
    return x**2/2/n + simpson(circle,x,0.5,NUM_INTERVALS)
    
#def integral(x):
#    return 1- (x/2)- (1- 2*x)/ 8* m.sqrt(-4* x**2 + 4* x+ 3)- 0.5* m.asin(0.5- x) 
    
def newton(x0,n):
    x_0 = x0
    while True: #x0-x1>10**-6:
        x_1 = x_0
        x_0 = x_0 - (b(x_0,n)/b_prime(x_0,n))      
        if m.fabs(x_0-x_1) < 10**(-10):
            return x_0
        
def simpson(f, a, b, n):
    """Approximates the definite integral of f from a to b by the
    composite Simpson's rule, using n subintervals (with n even)"""
    
    if n % 2:
        raise ValueError("n must be even (received n=%d)" % n)
    
    h = (b - a) / n
    s = f(a) + f(b)
    
    for i in range(1, n, 2):
        s += 4 * f(a + i * h)
    for i in range(2, n-1, 2):
        s += 2 * f(a + i * h)
    
    return s * h / 3
    
ratio = 1.0
threshold = 0.001
n=1
while ratio > threshold:
    ratio =  area(newton(0.3,n),n) / BASE_AREA 
    n+= 1
print("Ratio: " + str(ratio*100))
print("Number of Circles: " + str(n-1))
#newton(0.3,1)