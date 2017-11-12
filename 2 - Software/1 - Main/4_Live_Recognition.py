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

# Variable Declarations
isHandshakeDone = False
calibrated = False
debugLoops = 50
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
resend = ("\r\nR").encode()
reshapedBy = int(reshapeBy*12)

# Declare column headers
cols = ['ID', 'x0', 'y0', 'z0', 'x1', 'y1', 'z1', 'x2', 'y2', 'z2', 'x3', 'y3', 'z3']
fullDF = pd.DataFrame(columns=cols)

## Encode output variable
le = preprocessing.LabelEncoder()
le.fit(['Standing', 'WaveHands', 'BusDriver', 'FrontBack', 'SideStep', 'Jumping'])

## Functions
if (useServer):
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

#Load Models
knn_model = joblib.load('model_knn.pkl')
rf_model = joblib.load('model_rf.pkl')

sys.stdout.write("\033[F") # Cursor up one line
print("Initalized")

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
    sys.stdout.write("\033[F") # Cursor up one line
    print("Connected to server")

# Initialize Arduino connection
print("Connecting to Raspberry Pi")
ser = serial.Serial(arduinoPort, baudrate=115200, timeout=3.0)
sys.stdout.write("\033[F") # Cursor up one line
print("Raspberry Pi Connected")

# Perform handshake
while (isHandshakeDone != True):
        ser.write(handshake)
        print("H sent, awaiting response")
        response = ser.read()
        if response == 'A':
            sys.stdout.write("\033[F") # Cursor up one line
            print("Response verified, handshake complete")
            isHandshakeDone = True
            print("Starting in 2 seconds")
            time.sleep(2)
            ser.write(acknoledged)
        else:
            time.sleep(1)
            sys.stdout.write("\033[F") # Cursor up one line
            print("H sent, awaiting response.")
            time.sleep(1)
            sys.stdout.write("\033[F") # Cursor up one line
            print("H sent, awaiting response..")
            time.sleep(1)
            sys.stdout.write("\033[F") # Cursor up one line
            print("H sent, awaiting response...")
            time.sleep(1)
            sys.stdout.write("\033[F") # Cursor up one line

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

# Ignore first 50 readings
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
        print('Checksum matches. Message:', message)
        ser.write("\r\nA")
        # Store data into buffer
    else: # Checksums do not match
        print('Checksums do not match!')
        print("Message:", message)
        print("Checksum: \"", chr(checkSum), "\"")
        ser.write("\r\nR") # Send request for resend of data to Arduino
    ignoreLoopCount += 1
    checkSum = 0
    hashcount = 0
    print("Loop ", ignoreLoopCount, "took:", current_milli_time()-loopTime)
print("Average debug loop duration (ms): ", ((current_milli_time()-startTime)/10))

# Read (Main Loop)
print("SYSTEM LIVE")

while (loopCount < mainLoops):
    loopCount += 1
    message = ser.readline()
    #print(message)
    newAccID = int(message.split(',')[0])

    if (newAccID == oldAccID): # Check if ID incremented
        byteMessage = array.array('B', message)

        while hashcount < (len(byteMessage)-2): # Produce checksum from received data
                checkSum ^= int(byteMessage[hashcount])
                hashcount += 1

        if chr(checkSum) == message[len(message)-2]: # Check if checksums matches
            ser.write("\r\nA")
            messagenp = np.fromstring(message[0:(len(message)-2)], dtype=int, sep=",")
            messagepd = pd.DataFrame(data=messagenp.reshape(-1, (len(messagenp))), index=['1'], columns=cols)
            fullDF = fullDF.append(messagepd, ignore_index = True)
            successCount += 1
            oldAccID = newAccID + 1

        else: # Checksums do not match
            ser.write(resend) # Send request for resend of data from Arduino
            checkSumFailCount += 1
            print('Checksums do not match!')
            print("Recieved message:", message)
            print("Produced checksum:", chr(checkSum))

    else : # Unexpected/corrupt ID recieved
        ser.write(resend) # Send request for resend of data from Arduino
        IDFailCount += 1
        print(' ')
        print('ID MISMATCH')
        print('At Loop:', loopCount)
        print('Message:', message)
        print('oldAccID =', oldAccID)
        print('newAccID =', newAccID)
        #print("ENDING PROGRAM")
        #errorFlag = 1
        #loopCount = mainLoops
        #print('Resetting values to continue')
        #oldAccID = newAccID + 1

    # Reset values
    checkSum = 0
    hashcount = 0

    # Show user number of loops
    if (loopCount%300 == 0):
        print('At Loop:', loopCount)
        print('Successes', successCount)
        print('ID Fails', IDFailCount)
        print('Check Sum Fails', checkSumFailCount)

    # When number of
    if (successCount%reshapeBy == 0):

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

        #Send and print data in readable format
        sendEncoded((le.inverse_transform(rf_model.predict(normalized_X))), 1, 2, 3, 4)
        print('KNN:', (le.inverse_transform(knn_model.predict(normalized_X))), 'RF', (le.inverse_transform(rf_model.predict(normalized_X))))

        #Clear and reset variable
        del fullDF
        fullDF = pd.DataFrame(columns=cols)


# Remove unneeded data
fullDF = fullDF.drop(fullDF.columns[0], axis=1) # Remove ID

# Save cleaned raw data to csv file
fullDF.to_csv('recorded_data.csv', sep=',')
