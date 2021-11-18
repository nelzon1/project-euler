# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 23:33:29 2018

@author: jaken
"""

#create a dictionary of frequency to squares (list)
#create a dictionary of freuqency to words(list)
#
#for each item in word dictionary where len > 1:
#    for each square in matching square dictionary:
#        sub the square into the word
#        get mapping of letters to numbers
#        apply for any other words in the current word dictionary
#            are they in the corresponding squares list?
#            if yes, then add the larger of the 2 squares to a list of candidates:
                
def genSquare(inSquare,inWord,outWord):
    charToDigitMap = zip(inWord,str(inSquare))
    outSquare = str(outWord)
    for pair in charToDigitMap:
        outSquare=outSquare.replace(pair[0],pair[1])
    return outSquare

print(genSquare(1296,"CARE","RACE"))


import pandas as pd



with open("euler98.txt",'r') as dataFile:
    words = dataFile.read().replace('"','')
    words = [[x] for x in words.split(',')]
    words = pd.DataFrame.from_records(words,columns=["word"])
    
        
def initialize():

    squares = []

    for x in range(1,1000000):
        squares.append([x*x]) 
    squares = pd.DataFrame.from_records(squares,columns=['square'])
    
    return squares

try:    
    if (len (squares) == 0):
        squares = initialize()
except:
    squares = initialize()


def findMatchingWords(square):
    squareLen = len(str(square))
    return [x for x in words[words['word'].apply(lambda x: len(x)==squareLen) ]['word']]
    

def findMatchingSquares(word):
    temp = []
    for x in squares['square']:
        if len(str(x)) == len(str(word)):
            if sorted(frequency(word).values()) == sorted(frequency(x).values()):
                temp.append(x)
    return temp
    
def frequency(word):
    freq = {}
    for letter in sorted(str(word).upper()):
        try:
            freq[letter.upper()] = freq[letter.upper()]+1
        except KeyError:
            freq[letter.upper()] = 1
    return freq


def findAnagrams(word):
    composition = frequency(word)
    tempdf = pd.DataFrame.from_records([[x] for x in findMatchingWords(word)],columns=['word'])
    return [x for x in tempdf[tempdf['word'].apply(lambda x: frequency(x) == composition) ]['word']]
    
wordDictionary = {} #keys are a string the values in the corresponding digit map (string of a number)
#squareDictionary = {} #keys are a string the values in the corresponding digit map (string of a number)
    

for word in words['word']:
    freq = frequency(word)
    barcode = ''.join([str(x) for x in freq.values()])
    try:
        wordDictionary[barcode].append(word)
    except KeyError:
        wordDictionary[barcode] = [word]
        
        
'''for square in squares['square']:
    freq = frequency(square)
    barcode = ''.join([str(x) for x in freq.values()])
    try:
        squareDictionary[barcode].append(square)
    except KeyError:
        squareDictionary[barcode] = [square]'''

pairs = []

for word in words['word']:
    anagrams = findAnagrams(word)
    if len(anagrams) > 2 :
        pairs.append(sorted(anagrams[0:2]))
        pairs.append(sorted(anagrams[1:3]))
    elif len(anagrams) == 2 and sorted(anagrams) not in pairs:
        pairs.append(sorted(anagrams))

for pair in pairs:
    barcode = ''.join([str(x) for x in frequency(pair[0]).values()])
    candidates = squareDictionary[barcode]
    for x in candidates:
    #    compliment = genSquare(x,"REDUCTION","INTRODUCE")
        compliment = genSquare(x,pair[0],pair[1])
        for y in candidates:
            if str(compliment) == str(y):
                print (x, y)
            