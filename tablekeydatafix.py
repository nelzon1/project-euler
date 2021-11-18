# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 00:16:55 2017

@author: jaken
"""

import csv

tablef = open('tables.csv','r')

keyf = open('keys.csv','r')

csvreader = csv.reader(tablef)
tables = [x for x in csvreader]

csvreader = csv.reader(keyf)
keys = [x for x in csvreader]

tablef.close()
keyf.close()

last_table = ''
for k in keys:
    for t in tables:
        if k[0]==t[0] and k[1]==t[1]:
            t.append('K')
            break
        
for t in tables:
    if t[0] != last_table:
        t.append('P')
    last_table=t[0]
    
newtable = open('newtable.csv','w',newline='')
csvwriter = csv.writer(newtable)
csvwriter.writerows(tables)
newtable.close()