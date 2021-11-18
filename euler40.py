# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 18:05:36 2016

@author: jaken
"""

champernowne = ''

for i in range (1,300000):
    champernowne = champernowne + str(i)
    
#print (champernowne)
solution = int(champernowne[0]) * \
            int(champernowne[9]) * \
            int(champernowne[99]) * \
            int(champernowne[999]) * \
            int(champernowne[9999]) * \
            int(champernowne[99999]) * \
            int(champernowne[999999])
            
            
print (solution)