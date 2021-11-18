# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 19:48:32 2018

@author: jaken
"""

# Returns the count of ways we can sum
# S[0...m-1] coins to get sum n
def primesToN(n):
    primes = [True]*(n-1)
    for i in range(2, n//2 + 1):
        s = 2 * i
        while s <= n:
            primes[s-2] = False
            s += i
    plist = []
    for z in range(0,n-1): 
        if primes[z]:
            plist.append(z+2)
    return plist

def count(S, m, n ):
 
    # If n is 0 then there is 1
    # solution (do not include any coin)
    if (n == 0):
        return 1
 
    # If n is less than 0 then no
    # solution exists
    if (n < 0):
        return 0;
 
    # If there are no coins and n
    # is greater than 0, then no
    # solution exist
    if (m <=0 and n >= 1):
        return 0
 
    # count is sum of solutions (i) 
    # including S[m-1] (ii) excluding S[m-1]
    return count( S, m - 1, n ) + count( S, m, n-S[m-1] );

print (count([2,3,5,7],4,10))

primes = primesToN(1000)

cur = 0
z=10
while cur <=5000:
    primes = primesToN(z)
    cur = count(primes,len(primes),z)
    z+=1
print (z-1)
print(cur)