# -*- coding: utf-8 -*-
"""
@author: Jun Hao
"""

from Crypto.Cipher import AES
from Crypto import Random
import base64
import os, random
import socket
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

# Print current time on computer
print(str(datetime.now()))
print("Initalizing")

# Config.ini
reshapeBy = 40 # Set number of inputs per sample for Machine Learning
arduinoPort = "/dev/ttyACM0"
useServer = False
skipCalibration = True
key = '3002300230023002'

## Functions
def encryptData(data):
     BLOCK_SIZE = 16
     PADDING = ' '

     pad = lambda s: s + (BLOCK_SIZE - (len(s) % BLOCK_SIZE)) * PADDING

     iv = Random.new().read(AES.block_size)
     cipher = AES.new(key, AES.MODE_CBC, iv)
     encoded = base64.b64encode(iv + cipher.encrypt(pad(data)))
     #print('Encryption key: ', key)
     print('Encrypted string: ', encoded)
     return encoded

def sendEncoded(action, voltage, current, power, cumpower):
    msg = '#' + str(action) + '|' + str(voltage) + '|' + str(current) + '|' + str(power) + '|' + str(cumpower)
    client.send(encryptData(msg))

#Implement simple timer
current_milli_time = lambda: int(round(time.time() * 1000)) # current_milli_time()

# Variable Declarations
isHandshakeDone = False
calibrated = False
debugLoops = 200
mainLoops = 6000
ignoreLoopCount = 0
loopCount = 0
successCount = 0
checkSumFailCount = 0
IDFailCount = 0
newAccID = 0
oldAccID = debugLoops
oldTime = current_milli_time()
newTime = current_milli_time()
hashcount = 0
checkSum = 0
errorFlag = 0

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

#Load Models
knn_model = joblib.load('model_knn.pkl')
rf_model = joblib.load('model_rf.pkl')

#time.sleep(0.5)
sys.stdout.write("\033[F") # Cursor up one line
sys.stdout.write("\033[K") # Clear line
print ("Initalized")
#time.sleep(0.5)

# Initialize server connection
if (useServer):
    print("Connecting to server")
    client = socket.socket()
    ip = input("Enter IP:")
    #ip = socket.gethostbyname(socket.gethostname())
    port = int(input("Enter port: "))
    #port = 3002
    address = (ip,port)
    client.connect(address)
    #time.sleep(0.5)
    sys.stdout.write("\033[F") # Cursor up one line
    sys.stdout.write("\033[K") # Clear line
    print ("Connected to server")
    #time.sleep(0.5)

# Initialize Arduino connection and perform handshake
while (isHandshakeDone == False):
        print("Connecting to Raspberry Pi")
        ser = serial.Serial(arduinoPort, baudrate=115200, timeout=3.0)
        ser.write(handshake)
        time.sleep(0.2)
        ser.write(handshake)
        time.sleep(0.2)
        sys.stdout.write("\033[F") # Cursor up one line
        sys.stdout.write("\033[K") # Clear line
        print ("Raspberry Pi Connected")
        ser.write(handshake)
        print("H sent, awaiting response")
        response = ser.read()
        if response == (("A").encode()):
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
        else:
            ser.write(handshake)
            print(response)
            ser.write(handshake)

# Calibration
if (skipCalibration == False):
    startTime = current_milli_time()
    while (calibrated == False):
        # 1. read data
        # 2. check if any value exceed limits -> WARN WORN INCORRECT -> reset to step 1
        # 3. check if large fluctuation from any previous datas -> WARN LARGE FLUCTUATION -> reset to step 1
        # 3b. else save data and loop until count = 200 -> take average of 200 sets of data to be calibrateCandidate1
        # 4. ask user to move about and reset position to neutral -> give 5 seconds before starting
        # 5. restart from 1 for calibrateCandidate2
        # 6. check if calibrateCandidate1 is close to calibrateCandidate2, if yes, take the average and save calibration data

        calibrationPD = pd.DataFrame(data=calibrationNP.reshape(-1, (len(calibrationNP))), index=['1'], columns=cols)
    fullDF = fullDF.append(calibrationPD, ignore_index = True)
    print("Calibration took (ms): ", (current_milli_time()-startTime))

# Ignore early readings
print("Begin System Test")
startTime = current_milli_time()
loopTime = current_milli_time()
while (ignoreLoopCount < debugLoops):
    if (current_milli_time() > (loopTime+0)):
        loopTime = current_milli_time()
        message = ser.readline()
        byteMessage = array.array('b', message)
        message = message.decode()
        while hashcount < (len(byteMessage)-2): # Produce checksum from received data
            checkSum ^= int(byteMessage[hashcount])
            hashcount += 1
        if chr(checkSum) == message[len(message)-2]: #Check if checksums matches
            print('Checksum matches. Message:', message)
            ser.write(acknoledged)
            # Store data into buffer
        else: # Checksums do not match
            print('Checksums do not match!')
            print("Message:", message)
            print("Checksum: \"", chr(checkSum), "\"")
            ser.write(resend) # Send request for resend of data to Arduino
        ignoreLoopCount += 1
        checkSum = 0
        hashcount = 0
        print("Loop ", ignoreLoopCount, "took:", current_milli_time()-loopTime)
print("Average debug loop duration (ms): ", ((current_milli_time()-startTime)/debugLoops))
oldAccID = int(message.split(',')[0]) + 1

# Read (Main Loop)
print(' ')
print("SYSTEM LIVE")
print(" ")
startTime = current_milli_time()
loopTime = current_milli_time()

while (loopCount < mainLoops):
    if (current_milli_time() > (startTime+0)):
        startTime = current_milli_time()
        loopCount += 1
        messageB = ser.readline()
        message = messageB.decode()
        newAccID = int(message.split(',')[0])
        ser.write(acknoledged)

        if (newAccID == oldAccID): # Check if ID incremented
            byteMessage = array.array('b', messageB)

            while hashcount < (len(byteMessage)-2): # Produce checksum from received data
                    checkSum ^= int(byteMessage[hashcount])
                    hashcount += 1

            if chr(checkSum) == message[len(message)-2]: # Check if checksums matches
                messagenp = np.fromstring(message[0:(len(message)-2)], dtype=int, sep=",")
                messagepd = pd.DataFrame(data=messagenp.reshape(-1, (len(messagenp))), index=['1'], columns=cols)
                fullDF = fullDF.append(messagepd, ignore_index = True)
                successCount += 1
                oldAccID = newAccID + 1

            else: # Checksums do not match
                #ser.write(acknoledged) # Send request for resend of data from Arduino
                checkSumFailCount += 1
                errorFlag = True
                print(' ')
                print('Checksums do not match!')
                print("Recieved message:", message)
                sys.stdout.write("\033[F") # Cursor up one line
                print("Produced checksum:", chr(checkSum))
                print(' ')

        else : # Unexpected/corrupt ID recieved
            #ser.write(acknoledged) # Send request for resend of data from Arduino
            IDFailCount += 1
            errorFlag = True
            print(' ')
            print('ID MISMATCH')
            print('At Loop:', loopCount)
            print('Message:', message)
            sys.stdout.write("\033[F") # Cursor up one line
            print('oldAccID:', oldAccID)
            print('newAccID:', newAccID)
            print(' ')

        # Reset values
        checkSum = 0
        hashcount = 0

        # Discard previous data
        if (errorFlag):
             print("Resolving error")
             errorFlag = False
             time.sleep(0.1)
             message = ser.readline().decode()
             print('MessageFix1:', message)
             sys.stdout.write("\033[F") # Cursor up one line
             time.sleep(0.1)
             message = ser.readline().decode()
             print('MessageFix2:', message)
             sys.stdout.write("\033[F") # Cursor up one line
             time.sleep(0.1)
             message = ser.readline().decode()
             print('MessageFix3:', message)
             sys.stdout.write("\033[F") # Cursor up one line
             message = ser.readline().decode()
             print('MessageFix4:', message)
             sys.stdout.write("\033[F") # Cursor up one line
             print(' ')
             oldAccID = int(message.split(',')[0])
             successCount = 0
             #Clear and reset variable
             del fullDF
             fullDF = pd.DataFrame(columns=cols)
             loopTime = current_milli_time()
             
        # Show user number of loops
        if (loopCount%500 == 0):
            print('Consecutive Successes:', successCount, '| ID errors:', IDFailCount,'| Checksum errors:', checkSumFailCount)

        # When number of consecutive successful readings reaches reshapeBy
        if ((successCount > 0) & (successCount%reshapeBy == 0)):
            loopEndTime = current_milli_time()
            processingStartTime = current_milli_time()
            fullDF = fullDF.drop(fullDF.columns[0], axis=1) # Remove ID
            fullDF = pd.DataFrame(np.reshape(fullDF.values,(1,reshapedBy)),  columns=list(range(reshapedBy)))
            fullDF.to_csv('temp.csv', sep=',')

            #Sort data into columns -> For some reason can't extract class column using the better(next) method
            with open('temp.csv') as csvfile:
                reader=csv.reader(csvfile,delimiter=',')
                headers = next(reader)
                column = {}
                for h in headers:
                    column[h] = []
                for row in reader:
                    for h, v in zip(headers, row):
                        column[h].append(v)

            #Sort data into a whole array and extract necessary data
            testdata = np.genfromtxt ('temp.csv', delimiter=",")
            testdata = np.delete(testdata, (0), axis=0)
            X = testdata[:,list(range(1, reshapedBy))]

            #Normalize data
            normalized_X = preprocessing.normalize(X)

            #Get Result
            result = le.inverse_transform(knn_model.predict(normalized_X))
            
            #Send and print data in readable format
            if (useServer):
                sendEncoded(result, 1, 2, 3, 4)
            print('RF:', result, '| Average reading time:', (loopEndTime-loopTime)/reshapeBy, 'ms','| Processing time:', current_milli_time()-processingStartTime, 'ms')
            
            #Clear and reset variable
            del fullDF
            fullDF = pd.DataFrame(columns=cols)
            loopTime = current_milli_time()


# Remove unneeded data
fullDF = fullDF.drop(fullDF.columns[0], axis=1) # Remove ID

# Save cleaned raw data to csv file
fullDF.to_csv('recorded_data.csv', sep=',')
