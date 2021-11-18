# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 23:31:33 2017

@author: jaken
"""
#60158
#3618984963
#469849

#14475939855     939698  61

def is_square(apositiveint):
  x = apositiveint // 2
  seen = set([x])
  while x * x != apositiveint:
    x = (x + (apositiveint // x)) // 2
    if x in seen: return False
    seen.add(x)
  return True   

squares = set([x*x for x in range(1,10000000)])


#euler 66
stinkers = []
solutions = []
for x in range (2,1001):
    if x**(1/2) % 1 == 0:
        continue
    solved = False
    z =2
    while not solved:
        sol = ((z**2 - 1) / x)
        if sol%1>0.99999:
            sol = int(sol) + 1
        if z > 10000000:
            stinkers.append(int(x))
            break
      #  if z < 2:
       #     z+=1
        #    continue
       # if( sol**(1/2)%1 < 10**(-6) ) or (sol**(1/2)%1>0.999999):
        #    print(str(int(sol)) + '\t' + str(z) + '\t' + str(x))
        if sol % 1 == 0 and int(sol) in squares:
            solutions.append((int(z),int(x),int(sol**(1/2))))
            solved = True
            break
        '''
        if sol == 1.0:
            solutions.append((int(z),int(x),int(sol**(1/2))))
            solved = True
            break
        elif sol < 2.0:
            z+=1
            continue
        elif is_square( sol) :
            solutions.append((int(z),int(x),int(sol**(1/2))))
            solved = True
            break
        '''
        z+=1
largest = solutions[0]        
for s in solutions:
    if largest[0] < s[0]:
        largest = s
        
print(largest)