# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 21:26:37 2016

A repository of clever or useful methods I have come up with

@author: jaken
"""
from collections import Counter
import math as m

def primeSieve(n):
    primes = [[x,True] for x in range(0,n+1)]
    for i in range(2,n//2+1):
        temp = 2*i
        while temp <= n:
            primes[temp][1] = False
            temp += i
    sieve = [x[0] for x in primes if x[1]]
    return sieve[2:]

def powerFactor(num):
    temp = num
    factors = []
    primes = primeSieve(num//2)
    index = 0
    while temp not in primes:
        try:
            curPrime = primes[index]
        except IndexError:
            break
        if temp % curPrime == 0:
            factors.append(curPrime)
            temp /= curPrime
            continue
        else:
            index += 1
    factors.append(int(temp))
    return factors

def gcf(a,b):
    r1 = max([a,b]) % min([a,b])
    z = min([a,b])
    while r1!= 0:
        r2=r1
        r1 = z % r1
        z = r2
    return z

def num_divisors(int1):
    count = 2
    for j in range(2,int(int1/2)+1):
        if int1%j==0:
            count += 1
    return count
    
    
def pro_factor(n):
    factors = [1,n]
    for i in range (2,int(m.sqrt(n)) + 1):
        if n % i == 0:
            factors.append(i)
            if int(n/i) != i:
                factors.append(int(n/i))
    factors.sort()            
    return factors
    
    
def isprime(num):
    if num < 2:
        return 0
    for i in range(2,int(m.sqrt(num))+1):
        if num%i==0:
            return 0
    return 1      

def primesToN(n):
    primes = [True]*n
    for i in range(2, n//2 + 1):
        s = 2 * i
        while s < n:
            primes[s-2] = False
            s += i
    plist = []
    for z in range(0,n): 
        if primes[z]:
            plist.append(z+2)

def nPrimes(n):
        count = 1
        yield 2
        num = 3
        while count < n:
            if isprime(num):
                yield num
                num+=2
                count +=1
            else:
                num+=2    
    
    
def prime_list(n):
    result = [2]
    primes = 1
    number = 3
    while  primes < n:
        if isprime(number):
            result.append(number)
            primes+=1
        number+=2
    return result

def list_prime_factors(n):
    temp = n
    results=[]
    while not isprime(temp):
        for x in range(2,int(m.sqrt(temp))+1):       
            if isprime(x) and temp % x ==0:
                results.append(x)
                temp/=x
                break
    results.append(int(temp))
    return results

def simplify_prime_factors(factors):
    histo = Counter(factors)
    results = []
    for f in histo:
        results.append(f**histo[f])
    return results    
    
def biggest_prime_factor(number):
    notmax=1
    n=number
    prime_factor=2
    while(notmax):
        for i in range(2,n+1):
            if n%i==0 and isprime(i)==1:
                if(i>prime_factor):                
                    prime_factor = i
                n /= i
                n=int(n)                
                if n==1:
                        notmax=0
                break
    return prime_factor
    
    
def palindrome(number):
    for i in range(0,int((len(number))/2)):
        if number[i] != number[len(number)-1-i]:
            return 0
    return 1
    
def nodupes(num):
    dupe = []
    for digit in str(num):
        if (digit in dupe):
            return 0
        dupe.append(digit)
    return 1
    
def rotate(l, n):
    return l[n:] + l[:n]      
    
    
def digit_pow(x,y):
    str_x = str(int(x))
    sum_x = 0
    for i in str_x:
        sum_x += m.pow(int(i),y)
    return sum_x    
    
    
#returns position of letter in the alphabet a= 1, z = 26
def char_position(letter):
    return ord(letter) - 96

#Roman Numerals 

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
