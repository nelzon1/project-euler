# -*- coding: utf-8 -*-
"""
Created on Thu May 25 14:44:03 2017
 
@author: JNELSON
"""
 
import datetime, os, time, sys, subprocess
logFile = "QueueScriptLog.txt"
import win32com.client
shell = win32com.client.Dispatch("WScript.Shell")

 
def eta():
    #this will calculate the number of seconds until the next business day (Weekday) start from the current time
    #check current datetime, if it is:
    #after hours on M-Th: add day and set target time to 4:45 am
    #after hour fri or weekend : next monday 4:45
    current = datetime.datetime.now()
    target = current
    if (current.weekday() in (5,6)) or (current.weekday() == 4 and current.hour >= 5):
        while target.weekday() != 0:
            target+= datetime.timedelta(1)
    elif current.weekday() in (0,2,3,4,1) and current.hour >= 5:
        target+=datetime.timedelta(1)
           
    target = target.replace(hour=4,minute=55,second=0)
   
    return (target - current).total_seconds()
 
 
def sec_to_duration(n):
                days = n // 86400
                hours = (n - days * 86400) // 3600
                minutes = (n - days* 86400 - hours * 3600 ) // 60
                seconds = n % 60
 
                return str(days) + " days, " + str(hours) + " hours, " + str(minutes) + " mins, " + str(round(seconds,1)) + " sec, "
 
start = time.clock()
#time.sleep(0.5)
'''
try:
    fileLoc = sys.argv[2]
    scriptLoc = sys.argv[1]
except:
    sys.exit("Error: No file arguments specified. Use 'python " + sys.argv[0] + " <CMS script filename> <data filename>'")
'''
fileLoc = 'data.dat'
scriptLoc = 'test.acsauto'

 
while True:
    timeNow=datetime.datetime.now()
    '''
    if timeNow.weekday() in (5,6) or (timeNow.hour < 5 or timeNow.hour >=18):
       print ("Sleeping until " + (timeNow+datetime.timedelta(seconds=eta())).isoformat())
       time.sleep(0.5)
       for i in range(int(eta())):
           try:
               time.sleep(1)
           except KeyboardInterrupt:
               raise
               print("interrupted")
   '''
    if time.time() - os.path.getmtime(fileLoc) > 30:
        subprocess.run("taskkill /IM acs_ssh.exe", shell=True)
        
        time.sleep(1)
        #subprocess.run('START "" ' + scriptLoc, shell=True)
        shell.SendKeys("{ENTER}", 0) 
        print('run script')
        with open(fileLoc,'a') as data:        
            data.write('lol ')
        
        #time.sleep(30)
        with open(logFile,'a') as log:
            log.write("Process restarted at " + datetime.datetime.now().isoformat() + '\n')
    time.sleep(2)