# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 17:49:36 2016

@author: jaken
"""

import math as m

powers = []

for a in range (2,101):
    for b in range(2,101):
        powa = m.pow(a,b);
        if not powa in powers:
            powers.append(powa)
            
        
print(len(powers))