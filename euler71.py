# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 17:28:01 2017

@author: jaken
"""
'''
def farey_function(n, descending=False):
    """Print the nth Farey sequence, either ascending or descending."""
    a, b, c, d = 0, 1, 1, n
    f1 = (1,n)
    f2 = (1,n)
    if descending: 
        a, c = 1, n-1
    #print ("%d/%d" % (a,b))
    while (c <= n and not descending) or (a > 0 and descending):
        k = int((n + b) / d)
        a, b, c, d = c, d, (k*c-a), (k*d-b)
        f1 = f2
        f2 = (a,b)
        if f2 == (3,7):
            print (f1, f2)
        #print ("%d/%d" % (a,b))
            
farey_function(1000000)'''
descending = False
n = 8
a, b, c, d = 0, 1, 1, n
f1 = (1,n)
f2 = (1,n)
if descending: 
    a, c = 1, n-1
#print ("%d/%d" % (a,b))
while (c <= n and not descending) or (a > 0 and descending):
    k = int((n + b) / d)
    a, b, c, d = c, d, (k*c-a), (k*d-b)
    f1 = f2
    f2 = (a,b)
    if f2 == (3,7):
        print (f1, f2)
    #print ("%d/%d" % (a,b))