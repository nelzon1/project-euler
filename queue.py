# -*- coding: utf-8 -*-
"""
Created on Thu May 25 14:44:03 2017
 
@author: JNELSON
"""
 
import datetime, os, time, sys, subprocess, win32com.client
logFile = "QueueScriptLog.txt"
shell = win32com.client.Dispatch("WScript.Shell")
 
def eta():
    #this will calculate the number of seconds until the next business day (Weekday) start from the current time
    #check current datetime, if it is:
    #after hours on M-Th: add day and set target time to 5:45 am
    #after hour fri or weekend : next monday 5:45
    current = datetime.datetime.now()
    target = current
    if (current.weekday() in (5,6)) or (current.weekday() == 4 and current.hour >= 5):
        while target.weekday() != 0:
            target+= datetime.timedelta(1)
    elif current.weekday() in (0,2,3,4,1) and current.hour >= 5:
        target+=datetime.timedelta(1)
           
    target = target.replace(hour=5,minute=55,second=0)
   
    return (target - current).total_seconds()
 
 
def sec_to_duration(n):
                days = n // 86400
                hours = (n - days * 86400) // 3600
                minutes = (n - days* 86400 - hours * 3600 ) // 60
                seconds = n % 60
 
                return str(days) + " days " + str(hours) + " hours " + str(minutes) + " mins " + str(round(seconds,1)) + " sec "
 
start = time.clock()
time.sleep(0.5)

try:
    fileLoc = sys.argv[2]
    scriptLoc = sys.argv[1]
except:
    sys.exit("Error: No file arguments specified. Use 'python " + sys.argv[0] + " <CMS script filename> <data filename>'")
   
 
while True:
    timeNow=datetime.datetime.now()
    
    if timeNow.weekday() in (5,6) or (timeNow.hour < 5 or timeNow.hour >=20):
       print ("Sleeping until " + (timeNow+datetime.timedelta(seconds=eta())).isoformat())
       with open(logFile,'a') as log:
           log.write(datetime.datetime.now().isoformat() +", Sleeping until: " + (timeNow+datetime.timedelta(seconds=eta())).isoformat() + '\n')
       time.sleep(0.5)
       for i in range(int(eta())):
           try:
               time.sleep(1)
           except KeyboardInterrupt:
               raise
               print("interrupted")
 
    if time.time() - os.path.getmtime(fileLoc) > 25:
        subprocess.run("taskkill /IM acs_ssh.exe", shell=True)
        time.sleep(1)
        subprocess.run('START "" ' + scriptLoc, shell=True)
        time.sleep(3)
        shell.SendKeys("{ENTER}", 0) 
        print("Uptime: " + sec_to_duration(time.clock() - start))
        print ("Process restarted at " + datetime.datetime.now().isoformat())      
        with open(logFile,'a') as log:
            log.write(datetime.datetime.now().isoformat() + ', Process restarted' + ', ')
            log.write("Uptime: " + sec_to_duration(time.clock() - start) + '\n')
            
        start = time.clock()
    time.sleep(5)