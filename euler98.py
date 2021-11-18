# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 22:09:32 2018

@author: jaken
"""
import pandas as pd



with open("euler98.txt",'r') as dataFile:
    words = dataFile.read().replace('"','')
    words = [[x] for x in words.split(',')]
    words = pd.DataFrame.from_records(words,columns=["word"])
    
maxlen = 0
 
for word in words:
    print(word)    
    '''if len(word) > maxlen:
        maxlen = len(word)'''
        
        
def initialize():

    squares = []

    for x in range(1,10000000):
        squares.append([x*x]) 
    squares = pd.DataFrame.from_records(squares,columns=['square'])
    
    return squares

try:    
    if (len (squares) == 0):
        squares = initialize()
except:
    squares = initialize()

#
#take in a word
#find subset of squares that match its length
#try assigning digits to match chosen square
#for the chosen square, further reduce the choices by finding only other square with matching digit counts
#see if the resulting substitutions are in the dictionary
#if they are, keep a note of the square formed and update if bigger than largest so far

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
    
    
'''for word in words['word']:
    if len(findAnagrams(word)) > 1:
        print(findAnagrams(word))'''




print ( findMatchingSquares('SUSTAIN'))