# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 21:00:15 2016

@author: jaken
"""
number = 0
cancelled = []


for i in range (11,100):
    for j in range (11,100):
# ab/cd
      
        number = i/j
        if number >= 1:
            continue
        ab = str(i)
        cd = str(j)
        a = int(ab[0])
        b = int(ab[1])
        c = int(cd[0])
        d = int(cd[1])
        if a == 0 or b == 0 or c == 0 or d == 0:
            continue

        if int(a)/int(d) == number:
            if b == c :
                cancelled.append([ab,cd])

            
        
        if int(a)/int(c) == number:
            if b == d :
                cancelled.append([ab,cd])

        
        if int(b)/int(d) == number:
            if a == c:
                cancelled.append([ab,cd])

             
        
        if int(b)/int(c) == number:
            if a == d:
                cancelled.append([ab,cd])

            
print (cancelled)