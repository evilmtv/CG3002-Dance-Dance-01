# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 16:09:01 2017

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
#import sys
from datetime import datetime
import time

client = socket.socket()
ip = input("Enter IP:")
#ip = socket.gethostbyname(socket.gethostname())
port = int(input("Enter port: "))
#port = 3002
address = (ip,port)
client.connect(address)

def encryptData(data):
    BLOCK_SIZE = 16
    PADDING = ' '

    pad = lambda s: s + (BLOCK_SIZE - (len(s) % BLOCK_SIZE)) * PADDING

    key = '3002300230023002'
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encoded = base64.b64encode(iv + cipher.encrypt(pad(data)))
    #print('Encryption key: ', key)
    print('Encrypted string: ', encoded)
    return encoded

def sendEncoded(action, voltage, current, power, cumpower):
    msg = '#' + str(action) + '|' + str(voltage) + '|' + str(current) + '|' + str(power) + '|' + str(cumpower)
    client.send(encryptData(msg))

#Set print command to print to file
#sys.stdout = open("OutputComb.txt", "w")

# Config.ini
reshapeBy = 40 # Set number of inputs per sample for Machine Learning
reshapedBy = int(reshapeBy*12)

#Print current time on computer
print (str(datetime.now()))

#Implement simple timer
current_milli_time = lambda: int(round(time.time() * 1000))
#startTime = current_milli_time()
timetotalsegment = 0

##Encode output variable
le = preprocessing.LabelEncoder()
le.fit(['Standing', 'WaveHands', 'BusDriver', 'FrontBack', 'SideStep', 'Jumping'])

#Load Models
knn_model = joblib.load('model_knn.pkl')
rf_model = joblib.load('model_rf.pkl')

# Declarations
isHandshakeDone = 0
debugLoops = 50
mainLoops = 6000
ignoreLoopCount = 0
loopCount = 0
oneSegmentCounter = 0
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
ser = serial.Serial("/dev/ttyACM0", baudrate=115200, timeout=3.0)
print("Raspberry Pi Ready")

# Perform handshake
while isHandshakeDone == 0:
        ser.write("\r\nH")
        print("H sent, awaiting response...")
        response = ser.read()
        if response == 'A':
            print("Response verified, handshake complete")
            print("Begin reading:")
            isHandshakeDone = 1
            ser.write("\r\nA")
        else:
            time.sleep(3)

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
            ser.write("\r\nA")
            #print('Correct')
            #print(message)
            messagenp = np.fromstring(message[0:(len(message)-2)], dtype=int, sep=",")
            #print(messagenp)
            messagepd = pd.DataFrame(data=messagenp.reshape(-1, (len(messagenp))), index=['1'], columns=cols)
            #print(messagepd)
            fullDF = fullDF.append(messagepd, ignore_index = True)
            loopCount += 1
            oldAccID = newAccID + 1
            oneSegmentCounter = oneSegmentCounter + 1

        else: # Checksums do not match
            ser.write("\r\nA")
            loopCount += 1
            oldAccID = newAccID + 1
            #ser.write("\r\nR") # Send request for resend of data from Arduino
            print('Checksums do not match!')
            print("Message:", message)
            print("Checksum:", chr(checkSum))

    else :
        #ser.write("\r\nR") # Send request for resend of data from Arduino
        ser.write("\r\nA")
        print(' ')
        print('ID MISMATCH')
        print('At Loop:', loopCount)
        print('Message:', message)
        print('oldAccID =', oldAccID)
        print('newAccID =', newAccID)
        #print("ENDING PROGRAM")
        #errorFlag = 1
        #loopCount = mainLoops
        print('Resetting values to continue')
        oldAccID = newAccID + 1

    checkSum = 0
    hashcount = 0
    if (loopCount%100 == 0):
        print(loopCount)
    if (oneSegmentCounter == 40):
        oneSegmentCounter = 0

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

print('Average main loop duration (ms):', ((current_milli_time()-startTime)/mainLoops))
print(fullDF)

# Remove unneeded data
fullDF = fullDF.drop(fullDF.columns[0], axis=1) # Remove ID

# Save cleaned raw data to csv file
fullDF.to_csv('recorded_data.csv', sep=',')
