# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 15:46:47 2017

@author: jaken
"""
file = open('euler59.txt','r')
data = file.readline().split(',')
import time
output = open('euler59_output.txt','w')
#a-z is 97 - 121
a,b,c = 97,97,97
cypher = ['g','o','d']

triplets = list(zip(data[0::3],data[1::3],data[2::3]))

for i in range(0,1):
    for j in range(0,1):
        for k in range(0,1):
            
            message  = []
            for triple in triplets:
                for a,b in zip(triple,cypher):
                    message.append(chr(int(a) ^ ord(b)))       
            #print (''.join(cypher) + ' - ' + ''.join(message[:50]))
            output.write(''.join(cypher) + ' - ' +''.join(message) + '\n')
            #time.sleep(0.1)
            cypher[2]=chr(ord(cypher[2])+1)
        cypher[2]=chr(97)
        cypher[1] = chr(ord(cypher[1])+1)
    cypher[1]=chr(97)
    cypher[0] = chr(ord(cypher[0])+1)
output.close()

#cypher = 'god'
cypher = ['g','o','d']
message  = []
for triple in triplets:
    for a,b in zip(triple,cypher):
        message.append(int(a) ^ ord(b))       
print (sum(message))