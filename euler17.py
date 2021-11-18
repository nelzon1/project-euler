# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 21:26:25 2016

@author: jaken
"""

characters = ["",#0
              "one",#1
              "two",#2
              "three",#3
              "four",#5
              "five",#5
              "six",#6
              "seven",#7
              "eight",#8
              "nine",#9
              "ten",#10
              "eleven",#11
              "twelve",#12
              "thirteen",#13
              "fourteen",#14
              "fifteen",#15
              "sixteen",#16
              "seventeen",#17
              "eighteen",#18
              "nineteen",#19
              "twenty",#20
              "thirty",#21
              "forty",#22
              "fifty",#23
              "sixty",#24
              "seventy",#25
              "eighty",#26
              "ninety","""#27""" ]
              
def int2text(n):
    string = ""
    if n < 21:
        string = characters[n]
        return string
    x =str(n)

    for i in range(0,len(x)):
        
        char=int(x[(i)])
        if i == len(x)-2:
            if char == 1:
                string = string + characters[int(x[len(x)-1])+10]
                break
            elif char == 0:
                string = string + characters[char]
            else:    
                string = string + characters[char+18]
        else:
            string = string + characters[char]
            
    if len(x) == 3:
        if int(x[len(x)-1])==0 and int(x[len(x)-2]) == 0:
            string = string + "hundred"
        else:
            string = string + "hundredand"
    if len(x) == 4:
        string = string + "thousand"           
            
    return string
numbers = ""
for i in range(1,1001):
    numbers = numbers + int2text(i)
            
print(numbers)          
print(len(numbers))
            