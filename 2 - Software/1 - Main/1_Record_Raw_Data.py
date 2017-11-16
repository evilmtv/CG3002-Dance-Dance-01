# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 16:09:01 2017
@author: Jun Hao
"""

#Set print command to print to file
import sys
#sys.stdout = open("OutputComb.txt", "w")

#Print current time on computer
from datetime import datetime
print (str(datetime.now()))

#Implement simple timer
import time
current_milli_time = lambda: int(round(time.time() * 1000))
timetotalsegment = 0

import pandas as pd
import numpy as np
#import csv
import serial
import array

# Config.ini
reshapeBy = 40 # Set number of inputs per sample for Machine Learning
arduinoPort = "/dev/ttyACM0"

# Declarations
flag = 1
debugLoops = 10
mainLoops = 10 # Duration approx = mainLoops * 20ms
ignoreLoopCount = 0
loopCount = 0
newAccID = 0
oldAccID = 0
oldTime = current_milli_time()
newTime = current_milli_time()
hashcount = 0
checkSum = 0
errorFlag = 0
skipCalibration = True
calibrated = False
x0cal = 0
y0cal = 0
z0cal = 0
x1cal = 0
y1cal = 0
z1cal = 0
x2cal = 0
y2cal = 0
z2cal = 0
x3cal = 0
y3cal = 0
z3cal = 0
isHandshakeDone = False

# Variable Declarations
isHandshakeDone = False
calibrated = False
debugLoops = 5
debugFailCount = 0
mainLoops = 10
ignoreLoopCount = 0
loopCount = 0
successCount = 0
checkSumFailCount = 0
IDFailCount = 0
newAccID = 0
oldAccID = 0
oldTime = current_milli_time()
newTime = current_milli_time()
hashcount = 0
msgCheckSum = 0
checkSum = 0
errorFlag = 0

# Static Declarations
handshake = ("\r\nH").encode()
acknoledged = ("\r\nA").encode()
clear = ("\r\nAAAAAAAAAA").encode()
resend = ("\r\nR").encode()
reshapedBy = int(reshapeBy*12)

# Declare column headers
cols = [list(range(1, (12*reshapeBy)+1))] # 1-480
fullDF = pd.DataFrame(columns=cols)
#print(fullDF)

# Initialize Arduino connection and perform handshake
print("Connecting to Raspberry Pi")
ser = serial.Serial(arduinoPort, baudrate=115200, timeout=3.0)
sys.stdout.write("\033[F") # Cursor up one line
sys.stdout.write("\033[K") # Clear line
print ("Raspberry Pi Connected")
while (isHandshakeDone == False):
        ser.write(handshake)
        print("H sent, awaiting response")
        response = ser.read().decode()
        if response == ('A'):
            print("Response verified, handshake complete")
            isHandshakeDone = True
            ser.write(acknoledged)
            ser.readline() # Clear the screaming
            ser.write(acknoledged)
            print("Starting in 3 seconds")
            time.sleep(0.3)
            sys.stdout.write("\033[F") # Cursor up one line
            sys.stdout.write("\033[K") # Clear line
            print ("Starting in 2 seconds")
            time.sleep(0.3)
            sys.stdout.write("\033[F") # Cursor up one line
            sys.stdout.write("\033[K") # Clear line
            print ("Starting in 1 seconds")
            time.sleep(0.3)
            sys.stdout.write("\033[F") # Cursor up one line
            sys.stdout.write("\033[K") # Clear line
            print ("Begin")
        else:
            ser.write(handshake)
            print(response)
            ser.write(handshake)

# Ignore early readings
print("Begin System Test")
startTime = current_milli_time()
loopTime = current_milli_time()
while (ignoreLoopCount < debugLoops):
    if (current_milli_time() > (loopTime+0)):
        loopTime = readTime = current_milli_time()
        message = ser.readline() # Read message from Arduino
        readEndTime = current_milli_time()

        ser.write(acknoledged) # Instruct Arduino to prepare next set of data

        message = message.decode() # Convert to string to manipulate data
        print(message)
        newAccID = int(message.split(',', 1)[0]) # Extract message ID
        msgCheckSum = int((message.rsplit(',', 1)[1])[:-2]) # Extract message checksum
        message = message.rsplit(',', 1)[0] # Remove checksum from message
        byteMessage = array.array('b', message.encode()) # Convert back to byteMessage to generate hash

        if (newAccID == (oldAccID + 1)): # Check if ID Incremented
            oldAccID = newAccID
            while (hashcount < len(byteMessage)): # Produce checksum from received data
                checkSum ^= int(byteMessage[hashcount])
                hashcount += 1

            if (checkSum == msgCheckSum): #Check if checksums matches
                print('Checksum matches')
            else: # Checksums do not match
                debugFailCount += 1
                print('Checksums error!', "Message Checksum:", msgCheckSum, "Generated Checksum:", checkSum)
                print("Message:", message)
                print(' ')

        elif (newAccID == oldAccID):
            debugFailCount += 1
            print('Same message received!')
            print(' ')
        else:
            debugFailCount += 1
            print('ID error!', 'oldAccID:', oldAccID, 'newAccID:', newAccID)
            print("Message:", message)
            print(' ')

        ignoreLoopCount += 1
        checkSum = 0
        hashcount = 0
        oldAccID = newAccID
        print("In debug loop:", ignoreLoopCount, "Reading took:", readEndTime-readTime, "ms", "Others took:", current_milli_time()-readEndTime)

print("Average debug loop duration (ms): ", ((current_milli_time()-startTime)/debugLoops), "with", debugFailCount, "errors")

print("Starting in 3 seconds")
time.sleep(0.3)
sys.stdout.write("\033[F") # Cursor up one line
sys.stdout.write("\033[K") # Clear line
print ("Starting in 2 seconds")
time.sleep(0.3)
sys.stdout.write("\033[F") # Cursor up one line
sys.stdout.write("\033[K") # Clear line
print ("Starting in 1 seconds")
time.sleep(0.3)
sys.stdout.write("\033[F") # Cursor up one line
sys.stdout.write("\033[K") # Clear line
print ("Begin")

# Read (Main Loop)
print("MAIN LOOP")
startTime = current_milli_time()

while (loopCount < mainLoops):
    startTime = current_milli_time()
    loopCount += 1
    message = ser.readline() # Read message from Arduino
    ser.write(acknoledged) # Instruct Arduino to prepare next set of data
    message = message.decode() # Convert to string to manipulate data
    newAccID = int(message.split(',', 1)[0]) # Extract message ID
    volt = int(message.rsplit(',', 3)[1])
    amp = int(message.rsplit(',', 2)[1])
    msgCheckSum = int((message.rsplit(',', 1)[1])[:-2]) # Extract message checksum
    message = message.rsplit(',', 1)[0] # Remove checksum from message
    byteMessage = array.array('b', message.encode()) # Convert back to byteMessage to generate hash

    if (newAccID == (oldAccID + 1)): # Check if ID Incremented
        while (hashcount < len(byteMessage)): # Produce checksum from received data
            checkSum ^= int(byteMessage[hashcount])
            hashcount += 1

        if (checkSum == msgCheckSum): #Check if checksums matches
            message = message.rsplit(',', 2)[0] # Remove volt and amp from message
            message = message.split(',', 1)[1] # Remove ID from message
            messagenp = np.fromstring(message[0:(len(message))], dtype=int, sep=",")
            #print(messagenp)
            #messagenp = messagenp.reshape(1,-1)

            messagepd = pd.DataFrame(data=messagenp.reshape(-1, (len(messagenp))), index=['1'], columns=cols)
            #print(messagepd)
            fullDF = fullDF.append(messagepd, ignore_index = True)

            successCount += 1

        else: # Checksums do not match
            #ser.write(acknoledged) # Send request for resend of data from Arduino
            checkSumFailCount += 1
            errorFlag = True
            print('Checksums error!', "Message Checksum:", msgCheckSum, "Generated Checksum:", checkSum)
            print("Message:", message)
            print(' ')

    elif (newAccID == oldAccID): # Repeated message recieved
        IDFailCount += 1
        errorFlag = True
        print('ID error!', 'Same message received!')
        print(' ')
    else: # Unexpected/corrupt ID recieved
        IDFailCount += 1
        errorFlag = True
        print('ID error!', 'oldAccID:', oldAccID, 'newAccID:', newAccID)
        print("Message:", message)
        print(' ')

    # Reset values
    oldAccID = newAccID
    checkSum = 0
    hashcount = 0

    # Show user number of loops
    if (loopCount%5== 0):
        print('Successes:', successCount, '| ID errors:', IDFailCount,'| Checksum errors:', checkSumFailCount)


print('Average main loop duration (ms):', ((current_milli_time()-startTime)/mainLoops))
print(fullDF)

# Remove unneeded data
#fullDF = fullDF.drop(fullDF.columns[0], axis=1) # Remove ID
# Save cleaned raw data to csv file
fullDF.to_csv('recorded_data.csv', sep=',')
