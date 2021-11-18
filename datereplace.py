# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 00:26:37 2017

@author: jaken
"""
import re
mystr = 'Rep.SetProperty "Split/Skill","471" Rep.SetProperty "Date","06/08/17"\
        b = Rep.ExportData("C:\coding\Agent Queue Analysis\daily_phone.txt", 59, 0, True, True, True)\
        Rep.Quit'
        
def update_date(replacetxt, string):
    #with open(filename, 'r') as file:
    #    filedata = file.read()
        # Replace the target string
    reg1 = re.compile(r'\D\d{3}\D')
    regex = re.compile(r'"\d{2}/\d{2}/\d{2}"')
    string = re.sub(reg1, replacetxt, string)
    # Write the file out again
    return string
reg1 = re.compile(r'\D\d\d\D')       
mystr = update_date('"452"',mystr)
regexs = r'"\d{2}/\d{2}/\d{2}"'

print  (re.search(reg1,mystr))