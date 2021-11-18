# -*- coding: utf-8 -*-
"""
Created on Thu May 11 23:28:14 2017

@author: jaken
"""

from subprocess import Popen
import datetime
import time
start = time.clock()
#time.sleep(0.5)
i=1

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

#print(eta(datetime.datetime(2017,5,19,14,25)))


while True:
    timeNow=datetime.datetime.now()
    if timeNow.weekday() in (5,6) or (timeNow.hour < 5 or timeNow.hour >=18):
       
        print ("Sleeping until " + (timeNow+datetime.timedelta(seconds=eta())).isoformat())
        print ("Press ctrl + z to exit the script")
        
        time.sleep(0.5)
        for i in range(int(eta())):
                try:
                    time.sleep(1)
                except KeyboardInterrupt:
                    raise
                    print("interrupted")

    try:
        p = Popen("batch.bat", cwd=r"C:\Python27")
        print("Uptime: " + str((time.clock()-start)/3600) + " hours.")
        print(str(i) + " iterations complete.")
        i+=1
        time.sleep(0.5)
    except:
        print("File not found, process aborted.")
        print("Uptime: " + str((time.clock()-start)/3600) + " hours.")
        print(str(i) + " iterations completed.")
        raise
        break
        
