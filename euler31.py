# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 20:38:11 2016

@author: jaken
"""

penny = 1
two = 2
nickel = 5
dime = 10
twenty = 20
half = 50
dollar = 100
toonie = 200

count = 0
for p in range (0,201):
    for too in range (0,101):
        for n in range (0,41):
            for d in range (0,21):
                for t in range (0,11):
                    for h in range (0,5):
                        for do in range (0,3):
                            for to in range (0,2):
                                if (penny*p + two*too + nickel*n + dime*d + twenty*t + half*h + dollar*do + toonie*to == 200):
                                    count += 1
                                    
print (count)