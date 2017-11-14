# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 03:35:36 2017

@author: diary
"""
import pandas as pd
import numpy as np
import csv
from sklearn import preprocessing
from sklearn.externals import joblib
import serial
import array
import sys
from datetime import datetime
import time

# Config.ini
reshapeBy = 40 # Set number of inputs per sample for Machine Learning
arduinoPort = "COM3"
useServer = False
skipCalibration = True
key = '3002300230023002'

#Implement simple timer
current_milli_time = lambda: int(round(time.time() * 1000)) # current_milli_time()

# Variable Declarations
isHandshakeDone = False
calibrated = False
debugLoops = 50
debugFailCount = 0
mainLoops = 6000
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

#knn_model = joblib.load('model_knn.pkl')

# Static Declarations
handshake = ("\r\nH").encode()
acknoledged = ("\r\nA").encode()
clear = ("\r\nAAAAAAAAAA").encode()
resend = ("\r\nR").encode()
reshapedBy = int(reshapeBy*12)

# Declare column headers
cols = ['ID', 'x0', 'y0', 'z0', 'x1', 'y1', 'z1', 'x2', 'y2', 'z2', 'x3', 'y3', 'z3']
fullDF = pd.DataFrame(columns=cols)

## Encode output variable
le = preprocessing.LabelEncoder()
le.fit(['Standing', 'WaveHands', 'BusDriver', 'FrontBack', 'SideStep', 'Jumping'])


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
            ser.readline()
            print("Starting in 3 seconds")
            time.sleep(0.5)
            sys.stdout.write("\033[F") # Cursor up one line
            sys.stdout.write("\033[K") # Clear line
            print ("Starting in 2 seconds")
            time.sleep(0.5)
            ser.write(acknoledged)
            ser.readline()
            sys.stdout.write("\033[F") # Cursor up one line
            sys.stdout.write("\033[K") # Clear line
            print ("Starting in 1 seconds")
            time.sleep(0.5)
            sys.stdout.write("\033[F") # Cursor up one line
            sys.stdout.write("\033[K") # Clear line
            print ("Begin")
            ser.write(acknoledged)
        else:
            ser.write(handshake)
            print(response)
            ser.write(handshake)

print("SYSTEM LIVE")
print(" ")
startTime = current_milli_time()
loopTime = current_milli_time()

while (ignoreLoopCount < debugLoops):
    if (current_milli_time() > (startTime+0)):
            startTime = current_milli_time()
            loopCount += 1
    
            message = ser.readline() # Read message from Arduino
            ser.write(acknoledged) # Instruct Arduino to prepare next set of data
    
            message = message.decode() # Convert to string to manipulate data
            print(' ')
            print(' ')
            print(' ')
            print(' ')
            print(message)
            newAccID = int(message.split(',', 1)[0]) # Extract message ID
            volt = int(message.rsplit(',', 3)[1])
            amp = int(message.rsplit(',', 2)[1])
            msgCheckSum = int(message.rsplit(',',1)[1]) # Extract message checksum
            message = message.rsplit(',', 1)[0] # Remove checksum from message
            byteMessage = array.array('b', message.encode()) # Convert back to byteMessage to generate hash
    
            if (newAccID == (oldAccID + 1)): # Check if ID Incremented
                oldAccID = newAccID
                while (hashcount < len(byteMessage)): # Produce checksum from received data
                    checkSum ^= int(byteMessage[hashcount])
                    hashcount += 1  
    
                if (checkSum == msgCheckSum): #Check if checksums matches
                    message = message.rsplit(',', 2)[0] # Remove volt and amp from message
                    message = message.split(',', 1)[1] # Remove ID from message
                    messagenp = np.fromstring(message[0:(len(message))], dtype=int, sep=",")
                    X = messagenp
    
                    #Normalize data
                    normalized_X = preprocessing.normalize(X)
    
                    #Get Result
                    #result = le.inverse_transform(knn_model.predict(normalized_X))
                    #print(result)
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
            checkSum = 0
            hashcount = 0
