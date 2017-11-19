# -*- coding: utf-8 -*-
"""
@author: Jun Hao
"""

from Crypto.Cipher import AES
from Crypto import Random
import base64
import socket
import numpy as np
from scipy.stats import mode #https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.mode.html
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
reshapeBy = 50 # Set number of inputs per sample for Machine Learning
arduinoPort = "/dev/ttyACM0" # On Windows use arduinoPort = "COM3"
useServer = True
skipCalibration = True
key = '3002300230023002'
debugLoops = 3
mainLoops = 6000
skipCalibration = True
#sys.stdout = open("OutputComb.txt", "w") # Set print command to print to file

# Functions
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
debugFailCount = 0
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
resultBuffer =['standing', 'standing', 'standing', 'standing', 'standing']
cumpower = 0
resetFlag = False
resetFlagCount = 0
logoutCount = 0

# Static Declarations
handshake = ("\r\nH").encode()
acknoledged = ("\r\nA").encode()
clear = ("\r\nAAAAAAAAAA").encode()
resend = ("\r\nR").encode()

## Encode output variable
le = preprocessing.LabelEncoder()
le.fit(['standing', 'wavehands', 'busdriver', 'frontback', 'sidestep', 'jumping', 'jumpingjack', 'turnclap', 'squatturnclap', 'windowcleaning', 'windowcleaner360', 'logout'])


#Load Models
#knn_model = joblib.load('model_knn.pkl')
rf_model = joblib.load('model_rf.pkl')

sys.stdout.write("\033[F") # Cursor up one line
sys.stdout.write("\033[K") # Clear line
print ("Initalized")


# Initialize server connection
if (useServer):
    print("Connecting to server")
    client = socket.socket()
    #ip = input("Enter IP:")
    ip = '192.168.43.51'
    #ip = socket.gethostbyname(socket.gethostname())
    #port = int(input("Enter port: "))
    port = 8888
    address = (ip,port)
    client.connect(address)
    #time.sleep(0.5)
    sys.stdout.write("\033[F") # Cursor up one line
    sys.stdout.write("\033[K") # Clear line
    print ("Connected to server")
    #time.sleep(0.5)


# Initialize Arduino connection and perform handshake
print("Connecting to Raspberry Pi")
ser = serial.Serial(arduinoPort, baudrate=115200, timeout=3.0)
sys.stdout.write("\033[F") # Cursor up one line
sys.stdout.write("\033[K") # Clear line
print ("Raspberry Pi Connected")
while (isHandshakeDone == False):
        ser.write(handshake) # Initiate handshake on Arduino
        print("H sent, awaiting response")
        response = ser.read().decode()
        if response == ('A'):
            print("Response verified, handshake complete")
            isHandshakeDone = True
            ser.write(acknoledged)
            ser.readline() # Clear the screaming "AAAAAAAAAAAAAAAAA"
            time.sleep(0.5)
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
            ser.write(acknoledged) # Intentionally increase message ID to #2 to test ID error checking in system test section
        else:
            ser.write(handshake)
            print(response)
            ser.write(handshake)


# Calibration (NOT IMPLEMENTED)
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
        print("Calibration took (ms): ", (current_milli_time()-startTime))


# Ignore early readings (System test)
print("Begin System Test")
startTime = loopTime = current_milli_time()
while (ignoreLoopCount < debugLoops):
    if (current_milli_time() > (loopTime + 0)): # Variable to force interval between sample requests
        loopTime = readTime = current_milli_time()
        message = ser.readline() # Read message from Arduino
        readEndTime = current_milli_time()

        ser.write(acknoledged) # Instruct Arduino to prepare next set of data

        message = message.decode() # Convert to string to manipulate data
        print("Message:", message)
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
                print(' ')

        elif (newAccID == oldAccID):
            debugFailCount += 1
            print('Same message received!')
            print(' ')
        else:
            debugFailCount += 1
            print('ID error!', 'oldAccID:', oldAccID, 'newAccID:', newAccID)
            print(' ')

        ignoreLoopCount += 1
        checkSum = 0
        hashcount = 0
        oldAccID = newAccID
        print("In debug loop:", ignoreLoopCount, "Reading took:", readEndTime-readTime, "ms", "Others took:", current_milli_time()-readEndTime)

print("Average debug loop duration (ms): ", ((current_milli_time()-startTime)/debugLoops), "with", debugFailCount, "errors")

time.sleep(1)


# Read (Main Loop)
print(' ')
print('SYSTEM LIVE')
print(' ')
startTime = current_milli_time()
loopTime = current_milli_time()
powerOldTime = current_milli_time()

while (loopCount < mainLoops):
    if (current_milli_time() > (startTime+0)):
        startTime = current_milli_time()
        loopCount += 1

        message = ser.readline() # Read message from Arduino
        ser.write(acknoledged) # Instruct Arduino to prepare next set of data

        message = message.decode() # Convert to string to manipulate data
        newAccID = int(message.split(',', 1)[0]) # Extract message ID
        volt = int(message.rsplit(',', 3)[1]) # Extract voltage reading
        amp = int(message.rsplit(',', 2)[1]) # Extract current reading
        msgCheckSum = int((message.rsplit(',', 1)[1])[:-2]) # Extract message checksum
        message = message.rsplit(',', 1)[0] # Remove checksum from message
        byteMessage = array.array('b', message.encode()) # Convert back to byteMessage to generate hash

        if (newAccID == (oldAccID + 1)): # Check if ID Incremented
            while (hashcount < len(byteMessage)): # Produce checksum from received data
                checkSum ^= int(byteMessage[hashcount])
                hashcount += 1

            if (checkSum == msgCheckSum): # Check if checksums matches
                
                successCount += 1
                
                message = message.rsplit(',', 2)[0] # Remove volt and amp from message
                message = message.split(',', 1)[1] # Remove ID from message
                messagenp = np.fromstring(message[0:(len(message))], dtype=int, sep=",")
                messagenp = messagenp.reshape(1,-1)

                # Normalize data
                normalized_X = preprocessing.normalize(messagenp)

                # Generate result from sample and store in resultBuffer array
                result = le.inverse_transform(rf_model.predict(normalized_X))
                resultBuffer[successCount%5] = result

                # Convert readings to appropriate units and calculate power and cumulative power
                amp = (amp * 5 / 1023) / (10 / 10.1) / 10
                volt = volt / 102.3
                pwr = round(volt*amp, 4)
                cumpower = cumpower + pwr*((current_milli_time()-powerOldTime)/3600)
                powerOldTime = current_milli_time()

            else: # Checksums do not match
                checkSumFailCount += 1
                print('Checksums error!', "Message Checksum:", msgCheckSum, "Generated Checksum:", checkSum)
                print("Message:", message)
                print(' ')

        elif (newAccID == oldAccID): # Repeated message recieved
            IDFailCount += 1
            print('ID error!', 'Same message received!')
            print(' ')
        else: # Unexpected/corrupt ID recieved
            IDFailCount += 1
            print('ID error!', 'oldAccID:', oldAccID, 'newAccID:', newAccID)
            print("Message:", message)
            print(' ')

        # Reset values
        oldAccID = newAccID
        checkSum = 0
        hashcount = 0

        # Show user number of loops (For debug)
        #if (loopCount%10 == 0):
        #    print('Successes:', successCount, '| ID errors:', IDFailCount,'| Checksum errors:', checkSumFailCount)
        
        # Generate bestAnswer and confidence level
        bestAnswer = str((mode(resultBuffer))[0][0][0])
        bestAnswerConfidence = mode(resultBuffer)[1][0]
        if (bestAnswer == 'standing'):
            logoutCount = logoutCount + 1
            if (logoutCount == 20):
                bestAnswer = 'logout'
                bestAnswerConfidence = 3
                logoutCount = 0
        else: # Reset logoutCount when no longer standing
            logoutCount = 0
        
        # After system sends bestAnswer to the server, the system is prevented from sending any more for 10 ticks, allowing for user to have enough time to move on to the next move
        if (resetFlag == True):
            resetFlagCount = resetFlagCount + 1
            if (resetFlagCount == 10):
                resetFlag = False
                resetFlagCount = 0
        
        # Send data in the required format to the server
        if (resetFlag == False):
            if (useServer):
                if ((bestAnswer != 'standing') & (bestAnswerConfidence > 2)):
                    sendEncoded(bestAnswer, round(volt, 3), round(amp, 3), pwr, round(cumpower, 3))
                    resetFlag = True
            
        # Print live information on system in terminal
        print('Latest Result', result, 'Best Answer:', bestAnswer, 'Confidence:', bestAnswerConfidence, 'Volt:', round(volt, 3), 'Amp:', round(amp, 3), 'Watt:', pwr, 'KWh:', round(cumpower, 3))
