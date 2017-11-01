# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 16:09:01 2017

@author: Jun Hao
"""

#Set print command to print to file
#import sys
#sys.stdout = open("OutputComb.txt", "w")

#Print current time on computer
from datetime import datetime
print (str(datetime.now()))

#Implement simple timer
import time
current_milli_time = lambda: int(round(time.time() * 1000))
#startTime = current_milli_time()
timetotalsegment = 0

import pandas as pd
import numpy as np
#import csv
#from sklearn import preprocessing
import serial
import array


# Declarations
flag = 1
debugLoops = 20
mainLoops = 200
ignoreLoopCount = 0
loopCount = 0
newAccID = 0
oldAccID = debugLoops
oldTime = current_milli_time()
newTime = current_milli_time()
hashcount = 0
checkSum = 0
errorFlag = 0

# Declare column headers
cols = ['ID', 'x0', 'y0', 'z0', 'x1', 'y1', 'z1', 'x2', 'y2', 'z2', 'x3', 'y3', 'z3']
fullDF = pd.DataFrame(columns=cols)

# Initialize serial
ser = serial.Serial("/dev/ttyACM5", baudrate=115200, timeout=3.0)
print("Raspberry Pi Ready")

# Perform handshake
while flag == 1:
        ser.write("\r\nH")
        print("H sent, awaiting response...")
        response = ser.read()
        if response == 'A':
            print("Response verified, handshake complete")
            print("Begin reading:")
            flag = 0
            ser.write("\r\nA")
        else:
            time.sleep(3)

# Ignore first 20 readings
print("Ignoring starting readings")
startTime = current_milli_time()
while (ignoreLoopCount < debugLoops):
    loopTime = current_milli_time()
    message = ser.readline()
    byteMessage = array.array('B', message)
    while hashcount < (len(byteMessage)-2): # Produce checksum from received data
        checkSum ^= int(byteMessage[hashcount])
        hashcount += 1
    if chr(checkSum) == message[len(message)-2]: #Check if checksums matches
        print('Checksum matches. Message: \"', message, ""\"")
        ser.write("\r\nA")
        # Store data into buffer
    else: # Checksums do not match
        print('Checksums do not match!')
        print("Message: \"", message, "\"")
        print("Checksum: \"", chr(checkSum), "\"")
        ser.write("\r\nR") # Send request for resend of data to Arduino
    ignoreLoopCount += 1
    checkSum = 0
    hashcount = 0
    print("Loop ", ignoreLoopCount, " took: " current_milli_time()-loopTime)
print("Average debug loop duration (ms): ", ((current_milli_time()-startTime)/10))

print("MAIN LOOP")
startTime = current_milli_time()
# Read (Main Loop)
while (loopCount < mainLoops):

    message = ser.readline()
    #print(message)
    newAccID = int(message.split(',')[0])

    if (newAccID == oldAccID):
        byteMessage = array.array('B', message)
        while hashcount < (len(byteMessage)-2): # Produce checksum from received data
                checkSum ^= int(byteMessage[hashcount])
                hashcount += 1
        if chr(checkSum) == message[len(message)-2]: # Check if checksums matches
            #print('Correct')
            #print(message)
            messagenp = np.fromstring(message[0:(len(message)-2)], dtype=int, sep=",")

            #print(messagenp)
            messagepd = pd.DataFrame(data=messagenp.reshape(-1, (len(messagenp))), index=['1'], columns=cols)
            #print(messagepd)
            ser.write("\r\nA")
            fullDF = fullDF.append(messagepd, ignore_index = True)
            loopCount += 1
            oldAccID = newAccID + 1
        else: # Checksums do not match
            print('Checksums do not match!')
            print("Message: \"", message, "\"")
            print("Checksum: \"", chr(checkSum), "\"")
            ser.write("\r\nR") # Send request for resend of data to Arduino
    else :
        print('ID MISMATCH')
        print('oldAccID =', oldAccID)
        print('newAccID =', newAccID)
        print("ENDING PROGRAM")
        errorFlag = 1
        loopCount = mainLoops
    checkSum = 0
    hashcount = 0

if (errorFlag == 0):
    print('Average main loop duration (ms):', ((current_milli_time()-startTime)/mainLoops))

    print(fullDF)


    # Remove unneeded data
    #fullDF = fullDF.drop(fullDF.columns[14], axis=1)
    #fullDF = fullDF.drop(fullDF.columns[13], axis=1)
    fullDF = fullDF.drop(fullDF.columns[0], axis=1) # Remove ID
    # Save cleaned raw data to csv file
    fullDF.to_csv('recorded_data.csv', sep=',')
