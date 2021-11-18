# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 20:27:07 2017

@author: jaken
"""

'''

I - 1
IV - 4
V - 5
IX - 9
X - 10
XL - 40
L - 50
XC - 90
C - 100
CD - 400
D - 500
CM - 900
M - 1000

METHOD

roman - > arabic
right to left, go through the string and count how many there are of each
when the character changes, see if it is I X or C, as these could be 2-character digits
multiply each 'digit' quantity by its base-value and add them together


arabic -> roman:
right to left, numeral by numeral

'''

baseValues = {\
    'I': 1,\
    'IV': 4,\
    'V': 5,\
    'IX': 9,\
    'X': 10,\
    'XL': 40,\
    'L': 50,\
    'XC': 90,\
    'C': 100,\
    'CD': 400,\
    'D': 500,\
   'CM': 900,\
    'M': 1000}
baseSets = [('M',''),('C','D'),('X','L'),('I','V')]


def romanToArabic(num):
    #num is a string in all caps
    count =1
    vals = []
    stains = []
    for i,char in enumerate(num):
        double = False
        if i in stains:
            continue        
        if i == len(num) - 1:
            vals.append((char,count))     
            break
        z=1
        while char == num[i+z]:
            count+=1
            stains.append(i+z)      
            z+=1
            if i+z == len(num):
                break
        if char == 'I':
            if num[i+1] == 'V':
                vals.append(('IV',1))
                stains.append(i+1)
                double = True
            elif num[i+1] == 'X':
                vals.append(('IX',1))
                stains.append(i+1)
                double = True
        elif char == 'X':
            if num[i+1] == 'L':
                vals.append(('XL',1))
                stains.append(i+1)
                double = True
            elif num[i+1] == 'C':
                vals.append(('XC',1))
                stains.append(i+1)
                double = True
        elif char == 'C':
            if num[i+1] == 'D':
                vals.append(('CD',1))
                stains.append(i+1)
                double = True
            elif num[i+1] == 'M':
                vals.append(('CM',1)) 
                stains.append(i+1)
                double = True
        if not double:
            vals.append((char,count))        
            count = 1          
    value = 0
    for numeral in vals:
        value += numeral[1] * baseValues[numeral[0]]
    return value
       
print(romanToArabic('V'))            
            
def arabicToRoman(num):
    string = str(num)  
    roman = ''
    for i,digit in enumerate(string):
        z=4-len(string)+i
        if len(string) == 4 and digit == '4' and i == 0:
            roman += 'M' * 4
            continue
        if digit == '1':
            roman += baseSets[z][0]
        if digit == '2':
            roman += baseSets[z][0] * 2   
        if digit == '3':
            roman += baseSets[z][0] * 3   
        if digit == '4':
            roman += baseSets[z][0] +  baseSets[z][1]   
        if digit == '5':
            roman += baseSets[z][1] 
        if digit == '6':
            roman += baseSets[z][1] +  baseSets[z][0]
        if digit == '7':
            roman += baseSets[z][1] +  baseSets[z][0] * 2
        if digit == '8':
            roman += baseSets[z][1] +  baseSets[z][0] * 3
        if digit == '9':
            roman += baseSets[z][0] +  baseSets[z-1][0]
        if digit == '0':
            roman += ''
    return roman   

#########################################

numeral_map = tuple(zip(
    (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1),
    ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
    ))

def int_to_roman(i):
    result = []
    for integer, numeral in numeral_map:
        count = i // integer
        result.append(numeral * count)
        i -= integer * count
    return ''.join(result)

def roman_to_int(n):
    n=n.upper()
    i = result = 0
    for integer, numeral in numeral_map:
        while n[i:i + len(numeral)] == numeral:
            result += integer
            i += len(numeral)
    return result
    
#######################################



     
#print(arabicToRoman(18))

with open('euler89.txt','r') as data:
    numerals = data.readlines()
    
romans = [x[:-1] for x in numerals]

difference = 0
romans_small = []
arabic=[]
romanchecker=[]
intchecker=[]
for z in romans:   
    romans_small.append(arabicToRoman(romanToArabic(z)))
    difference += len(z) - len(romans_small[-1])
    arabic.append(str(romanToArabic(z)))
    intchecker.append(str(roman_to_int(z)))
    romanchecker.append(int_to_roman(roman_to_int(z)))
    
print (difference)

with open('euler89.csv','w') as output:     
    for z in zip(romans,romans_small,arabic,intchecker,romanchecker):
        output.write(','.join(z) + '\n')


