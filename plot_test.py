# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 19:32:05 2017

@author: jaken
"""
colours = ['b',	'g',	'r',	'c',	'm',	'y',	'k',	'b']	

markers = ['o','v','^','s','D','*','+','x']


import matplotlib.pyplot as plt
import numpy as np


##############################################
#PRINT A BAR CHART WITH NAMES UNDERNEATH AND A LINE GRAPH OVERTOP
fig = plt.subplot()
calls,avg,acd = np.loadtxt('stats.csv',delimiter=',',skiprows=1,usecols=(1,2,3), unpack=True)
agents = np.loadtxt('stats.csv',dtype='str',delimiter=',',skiprows=1, usecols=(0,) )
'''
calls = data[:,1]
avg = data[:,2]
acd = data[:,3]
'''
agentz = []
for agent in agents:
    agentz.append(agent[2:-1])
agentz = tuple(agentz)
z= np.arange(8)
fig.bar(z-0.25,calls,0.5)
fig.set_xticks(z)
fig.set_xticklabels(agentz)
fig.set_xlabel('Agent')
fig.set_ylabel('Calls')
fig.set_title('Calls Taken Per Agent')
fig.plot(avg, 'r')
plt.show()
plt.savefig('plot.png',bbox_inches='tight')

#plt.close()
################################################

fig, ax = plt.subplots()

data = np.loadtxt('hist.csv',delimiter=',',dtype=bytes).astype(str)
agents = data[1:,0]
months = data[0,1:]
datez = data[1:,1:].astype(np.float)

for series,colour,marker,agent in zip(datez, colours, markers,agents):
    ax.plot(series,str(colour + marker + '--'), label=agent)
ax.legend()
ax.set_xticks(range(len(months)))
ax.set_xticklabels(months)
ax.set_xlabel('Month')
ax.set_ylabel('Calls Taken')
ax.set_title('Agent Calls Taken Month to Month')
plt.show()    
