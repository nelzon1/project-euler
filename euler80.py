# -*- coding: utf-8 -*-

"""

Created on Tue Jan 30 14:55:09 2018

 

@author: jnelson

"""

x=5.3

from itertools import zip_longest

def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)

def sqrt(x,n):
    decimal = ''
    if '.' in str(x):
        whole,decimal = str(x).split('.')
    else:
        whole = str(x)
    if len(whole)%2==1:
        whole = '0'+whole
    if len(decimal)%2==1:
        decimal += '0'
    digits = ''
    known= 0
    g = grouper(whole,2)
    limit = int(''.join(next(g) ))
    while len(digits) < n:
        dig = 0
        nxt = 0
        try:
            nxt = int(''.join(next(g) ))
        except StopIteration:
            print('iteration complete')
        for i in range(1,10):
            if known * 20 + nxt > limit:
                digits.append(i)
                break
    print(dig)
    print(list(grouper(whole,2)),list(grouper(decimal,2)))

sqrt(x,2)