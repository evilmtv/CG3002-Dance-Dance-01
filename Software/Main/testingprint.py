# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 13:13:18 2017

@author: diary
"""

#Implement simple timer
import time
current_milli_time = lambda: int(round(time.time() * 1000))
#startTime = current_milli_time()
timetotalsegment = 0

ignoreLoopCount = 23
loopTime=current_milli_time()
startTime=current_milli_time()

print("Loop\"", ignoreLoopCount, "\" took: ", current_milli_time()-loopTime)
print("Average debug loop duration (ms): ", ((current_milli_time()-startTime)/10))