# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 03:38:27 2017

@author: diary
"""

import serial
import time
import pandas as pd
import numpy as np
from sklearn import preprocessing
import sys

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
oldAccID = debugLoops
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
cols = ['ID', 'x0', 'y0', 'z0', 'x1', 'y1', 'z1', 'x2', 'y2', 'z2', 'x3', 'y3', 'z3']
fullDF = pd.DataFrame(columns=cols)

## Encode output variable
le = preprocessing.LabelEncoder()
le.fit(['Standing', 'WaveHands', 'BusDriver', 'FrontBack', 'SideStep', 'Jumping'])


# Initialize Arduino connection and perform handshake
while (isHandshakeDone == False):
        print("Connecting to Raspberry Pi")
        ser = serial.Serial(arduinoPort, baudrate=115200, timeout=3.0)
        sys.stdout.write("\033[F") # Cursor up one line
        sys.stdout.write("\033[K") # Clear line
        print ("Raspberry Pi Connected")
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