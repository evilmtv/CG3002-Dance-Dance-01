# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 16:39:56 2017

@author: diary
"""
import pandas as pd
import numpy as np
#import csv
#from sklearn import preprocessing

toAvg = 0
avgBy = 5
toReshape = 1
reshapeBy = 20

fullDF = pd.DataFrame(columns=list(range(241)))



pdtestdata = pd.read_csv('nic0.csv', delimiter=',')
pdtestdata = pdtestdata.drop(pdtestdata.columns[0], axis=1) # Remove ID
#print(pdtestdata)

if (toAvg):
    pdtestdata = ((pdtestdata + pdtestdata.shift(-1) + pdtestdata.shift(-2) + pdtestdata.shift(-3) + pdtestdata.shift(-4)) / 5)[::5]

if (toReshape):
    pdtestdata = pd.DataFrame(np.reshape(pdtestdata.values,(300,240)),  columns=list(range(240)))

pdtestdata = pdtestdata.reset_index(drop=True)
pdtestdata[240]='Standing'
#print(pdtestdata)
fullDF = fullDF.append(pdtestdata, ignore_index = True)
del pdtestdata



pdtestdata = pd.read_csv('nic1.csv', delimiter=',')
pdtestdata = pdtestdata.drop(pdtestdata.columns[0], axis=1) # Remove ID
#print(pdtestdata)

if (toAvg):
    pdtestdata = ((pdtestdata + pdtestdata.shift(-1) + pdtestdata.shift(-2) + pdtestdata.shift(-3) + pdtestdata.shift(-4)) / 5)[::5]

if (toReshape):
    pdtestdata = pd.DataFrame(np.reshape(pdtestdata.values,(300,240)),  columns=list(range(240)))

pdtestdata = pdtestdata.reset_index(drop=True)
pdtestdata[240]='WaveHands'
#print(pdtestdata)
fullDF = fullDF.append(pdtestdata, ignore_index = True)
del pdtestdata



pdtestdata = pd.read_csv('nic2.csv', delimiter=',')
pdtestdata = pdtestdata.drop(pdtestdata.columns[0], axis=1) # Remove ID
#print(pdtestdata)

if (toAvg):
    pdtestdata = ((pdtestdata + pdtestdata.shift(-1) + pdtestdata.shift(-2) + pdtestdata.shift(-3) + pdtestdata.shift(-4)) / 5)[::5]

if (toReshape):
    pdtestdata = pd.DataFrame(np.reshape(pdtestdata.values,(300,240)),  columns=list(range(240)))

pdtestdata = pdtestdata.reset_index(drop=True)
pdtestdata[240]='BusDriver'
#print(pdtestdata)
fullDF = fullDF.append(pdtestdata, ignore_index = True)
del pdtestdata



pdtestdata = pd.read_csv('nic3.csv', delimiter=',')
pdtestdata = pdtestdata.drop(pdtestdata.columns[0], axis=1) # Remove ID
#print(pdtestdata)

if (toAvg):
    pdtestdata = ((pdtestdata + pdtestdata.shift(-1) + pdtestdata.shift(-2) + pdtestdata.shift(-3) + pdtestdata.shift(-4)) / 5)[::5]

if (toReshape):
    pdtestdata = pd.DataFrame(np.reshape(pdtestdata.values,(300,240)),  columns=list(range(240)))

pdtestdata = pdtestdata.reset_index(drop=True)
pdtestdata[240]='FrontBack'
#print(pdtestdata)
fullDF = fullDF.append(pdtestdata, ignore_index = True)
del pdtestdata



pdtestdata = pd.read_csv('nic4.csv', delimiter=',')
pdtestdata = pdtestdata.drop(pdtestdata.columns[0], axis=1) # Remove ID
#print(pdtestdata)

if (toAvg):
    pdtestdata = ((pdtestdata + pdtestdata.shift(-1) + pdtestdata.shift(-2) + pdtestdata.shift(-3) + pdtestdata.shift(-4)) / 5)[::5]

if (toReshape):
    pdtestdata = pd.DataFrame(np.reshape(pdtestdata.values,(300,240)),  columns=list(range(240)))

pdtestdata = pdtestdata.reset_index(drop=True)
pdtestdata[240]='SideStep'
#print(pdtestdata)
fullDF = fullDF.append(pdtestdata, ignore_index = True)
del pdtestdata



pdtestdata = pd.read_csv('nic5.csv', delimiter=',')
pdtestdata = pdtestdata.drop(pdtestdata.columns[0], axis=1) # Remove ID
#print(pdtestdata)

if (toAvg):
    pdtestdata = ((pdtestdata + pdtestdata.shift(-1) + pdtestdata.shift(-2) + pdtestdata.shift(-3) + pdtestdata.shift(-4)) / 5)[::5]

if (toReshape):
    pdtestdata = pd.DataFrame(np.reshape(pdtestdata.values,(300,240)),  columns=list(range(240)))

pdtestdata = pdtestdata.reset_index(drop=True)
pdtestdata[240]='Jumping'
#print(pdtestdata)
fullDF = fullDF.append(pdtestdata, ignore_index = True)
del pdtestdata



pdtestdata = pd.read_csv('Raph0.csv', delimiter=',')
pdtestdata = pdtestdata.drop(pdtestdata.columns[0], axis=1) # Remove ID
#print(pdtestdata)

if (toAvg):
    pdtestdata = ((pdtestdata + pdtestdata.shift(-1) + pdtestdata.shift(-2) + pdtestdata.shift(-3) + pdtestdata.shift(-4)) / 5)[::5]

if (toReshape):
    pdtestdata = pd.DataFrame(np.reshape(pdtestdata.values,(300,240)),  columns=list(range(240)))

pdtestdata = pdtestdata.reset_index(drop=True)
pdtestdata[240]='Standing'
#print(pdtestdata)
fullDF = fullDF.append(pdtestdata, ignore_index = True)
del pdtestdata



pdtestdata = pd.read_csv('Raph1.csv', delimiter=',')
pdtestdata = pdtestdata.drop(pdtestdata.columns[0], axis=1) # Remove ID
#print(pdtestdata)

if (toAvg):
    pdtestdata = ((pdtestdata + pdtestdata.shift(-1) + pdtestdata.shift(-2) + pdtestdata.shift(-3) + pdtestdata.shift(-4)) / 5)[::5]

if (toReshape):
    pdtestdata = pd.DataFrame(np.reshape(pdtestdata.values,(300,240)),  columns=list(range(240)))

pdtestdata = pdtestdata.reset_index(drop=True)
pdtestdata[240]='WaveHands'
#print(pdtestdata)
fullDF = fullDF.append(pdtestdata, ignore_index = True)
del pdtestdata



pdtestdata = pd.read_csv('Raph2.csv', delimiter=',')
pdtestdata = pdtestdata.drop(pdtestdata.columns[0], axis=1) # Remove ID
#print(pdtestdata)

if (toAvg):
    pdtestdata = ((pdtestdata + pdtestdata.shift(-1) + pdtestdata.shift(-2) + pdtestdata.shift(-3) + pdtestdata.shift(-4)) / 5)[::5]

if (toReshape):
    pdtestdata = pd.DataFrame(np.reshape(pdtestdata.values,(300,240)),  columns=list(range(240)))

pdtestdata = pdtestdata.reset_index(drop=True)
pdtestdata[240]='BusDriver'
#print(pdtestdata)
fullDF = fullDF.append(pdtestdata, ignore_index = True)
del pdtestdata



pdtestdata = pd.read_csv('Raph3.csv', delimiter=',')
pdtestdata = pdtestdata.drop(pdtestdata.columns[0], axis=1) # Remove ID
#print(pdtestdata)

if (toAvg):
    pdtestdata = ((pdtestdata + pdtestdata.shift(-1) + pdtestdata.shift(-2) + pdtestdata.shift(-3) + pdtestdata.shift(-4)) / 5)[::5]

if (toReshape):
    pdtestdata = pd.DataFrame(np.reshape(pdtestdata.values,(300,240)),  columns=list(range(240)))

pdtestdata = pdtestdata.reset_index(drop=True)
pdtestdata[240]='FrontBack'
#print(pdtestdata)
fullDF = fullDF.append(pdtestdata, ignore_index = True)
del pdtestdata



pdtestdata = pd.read_csv('Raph4.csv', delimiter=',')
pdtestdata = pdtestdata.drop(pdtestdata.columns[0], axis=1) # Remove ID
#print(pdtestdata)

if (toAvg):
    pdtestdata = ((pdtestdata + pdtestdata.shift(-1) + pdtestdata.shift(-2) + pdtestdata.shift(-3) + pdtestdata.shift(-4)) / 5)[::5]

if (toReshape):
    pdtestdata = pd.DataFrame(np.reshape(pdtestdata.values,(300,240)),  columns=list(range(240)))

pdtestdata = pdtestdata.reset_index(drop=True)
pdtestdata[240]='SideStep'
#print(pdtestdata)
fullDF = fullDF.append(pdtestdata, ignore_index = True)
del pdtestdata



pdtestdata = pd.read_csv('Raph5.csv', delimiter=',')
pdtestdata = pdtestdata.drop(pdtestdata.columns[0], axis=1) # Remove ID
#print(pdtestdata)

if (toAvg):
    pdtestdata = ((pdtestdata + pdtestdata.shift(-1) + pdtestdata.shift(-2) + pdtestdata.shift(-3) + pdtestdata.shift(-4)) / 5)[::5]

if (toReshape):
    pdtestdata = pd.DataFrame(np.reshape(pdtestdata.values,(300,240)),  columns=list(range(240)))

pdtestdata = pdtestdata.reset_index(drop=True)
pdtestdata[240]='Jumping'
#print(pdtestdata)
fullDF = fullDF.append(pdtestdata, ignore_index = True)
del pdtestdata



pdtestdata = pd.read_csv('manish0.csv', delimiter=',')
pdtestdata = pdtestdata.drop(pdtestdata.columns[0], axis=1) # Remove ID
#print(pdtestdata)

if (toAvg):
    pdtestdata = ((pdtestdata + pdtestdata.shift(-1) + pdtestdata.shift(-2) + pdtestdata.shift(-3) + pdtestdata.shift(-4)) / 5)[::5]

if (toReshape):
    pdtestdata = pd.DataFrame(np.reshape(pdtestdata.values,(300,240)),  columns=list(range(240)))

pdtestdata = pdtestdata.reset_index(drop=True)
pdtestdata[240]='Standing'
#print(pdtestdata)
fullDF = fullDF.append(pdtestdata, ignore_index = True)
del pdtestdata



pdtestdata = pd.read_csv('manish1.csv', delimiter=',')
pdtestdata = pdtestdata.drop(pdtestdata.columns[0], axis=1) # Remove ID
#print(pdtestdata)

if (toAvg):
    pdtestdata = ((pdtestdata + pdtestdata.shift(-1) + pdtestdata.shift(-2) + pdtestdata.shift(-3) + pdtestdata.shift(-4)) / 5)[::5]

if (toReshape):
    pdtestdata = pd.DataFrame(np.reshape(pdtestdata.values,(300,240)),  columns=list(range(240)))

pdtestdata = pdtestdata.reset_index(drop=True)
pdtestdata[240]='WaveHands'
#print(pdtestdata)
fullDF = fullDF.append(pdtestdata, ignore_index = True)
del pdtestdata



pdtestdata = pd.read_csv('manish2.csv', delimiter=',')
pdtestdata = pdtestdata.drop(pdtestdata.columns[0], axis=1) # Remove ID
#print(pdtestdata)

if (toAvg):
    pdtestdata = ((pdtestdata + pdtestdata.shift(-1) + pdtestdata.shift(-2) + pdtestdata.shift(-3) + pdtestdata.shift(-4)) / 5)[::5]

if (toReshape):
    pdtestdata = pd.DataFrame(np.reshape(pdtestdata.values,(300,240)),  columns=list(range(240)))

pdtestdata = pdtestdata.reset_index(drop=True)
pdtestdata[240]='BusDriver'
#print(pdtestdata)
fullDF = fullDF.append(pdtestdata, ignore_index = True)
del pdtestdata



pdtestdata = pd.read_csv('manish3.csv', delimiter=',')
pdtestdata = pdtestdata.drop(pdtestdata.columns[0], axis=1) # Remove ID
#print(pdtestdata)

if (toAvg):
    pdtestdata = ((pdtestdata + pdtestdata.shift(-1) + pdtestdata.shift(-2) + pdtestdata.shift(-3) + pdtestdata.shift(-4)) / 5)[::5]

if (toReshape):
    pdtestdata = pd.DataFrame(np.reshape(pdtestdata.values,(300,240)),  columns=list(range(240)))

pdtestdata = pdtestdata.reset_index(drop=True)
pdtestdata[240]='FrontBack'
#print(pdtestdata)
fullDF = fullDF.append(pdtestdata, ignore_index = True)
del pdtestdata



pdtestdata = pd.read_csv('manish4.csv', delimiter=',')
pdtestdata = pdtestdata.drop(pdtestdata.columns[0], axis=1) # Remove ID
#print(pdtestdata)

if (toAvg):
    pdtestdata = ((pdtestdata + pdtestdata.shift(-1) + pdtestdata.shift(-2) + pdtestdata.shift(-3) + pdtestdata.shift(-4)) / 5)[::5]

if (toReshape):
    pdtestdata = pd.DataFrame(np.reshape(pdtestdata.values,(300,240)),  columns=list(range(240)))

pdtestdata = pdtestdata.reset_index(drop=True)
pdtestdata[240]='SideStep'
#print(pdtestdata)
fullDF = fullDF.append(pdtestdata, ignore_index = True)
del pdtestdata



pdtestdata = pd.read_csv('manish5.csv', delimiter=',')
pdtestdata = pdtestdata.drop(pdtestdata.columns[0], axis=1) # Remove ID
#print(pdtestdata)

if (toAvg):
    pdtestdata = ((pdtestdata + pdtestdata.shift(-1) + pdtestdata.shift(-2) + pdtestdata.shift(-3) + pdtestdata.shift(-4)) / 5)[::5]

if (toReshape):
    pdtestdata = pd.DataFrame(np.reshape(pdtestdata.values,(300,240)),  columns=list(range(240)))

pdtestdata = pdtestdata.reset_index(drop=True)
pdtestdata[240]='Jumping'
#print(pdtestdata)
fullDF = fullDF.append(pdtestdata, ignore_index = True)
del pdtestdata



pdtestdata = pd.read_csv('jun0.csv', delimiter=',')
pdtestdata = pdtestdata.drop(pdtestdata.columns[0], axis=1) # Remove ID
#print(pdtestdata)

if (toAvg):
    pdtestdata = ((pdtestdata + pdtestdata.shift(-1) + pdtestdata.shift(-2) + pdtestdata.shift(-3) + pdtestdata.shift(-4)) / 5)[::5]

if (toReshape):
    pdtestdata = pd.DataFrame(np.reshape(pdtestdata.values,(300,240)),  columns=list(range(240)))

pdtestdata = pdtestdata.reset_index(drop=True)
pdtestdata[240]='Standing'
#print(pdtestdata)
fullDF = fullDF.append(pdtestdata, ignore_index = True)
del pdtestdata



pdtestdata = pd.read_csv('jun1.csv', delimiter=',')
pdtestdata = pdtestdata.drop(pdtestdata.columns[0], axis=1) # Remove ID
#print(pdtestdata)

if (toAvg):
    pdtestdata = ((pdtestdata + pdtestdata.shift(-1) + pdtestdata.shift(-2) + pdtestdata.shift(-3) + pdtestdata.shift(-4)) / 5)[::5]

if (toReshape):
    pdtestdata = pd.DataFrame(np.reshape(pdtestdata.values,(300,240)),  columns=list(range(240)))

pdtestdata = pdtestdata.reset_index(drop=True)
pdtestdata[240]='WaveHands'
#print(pdtestdata)
fullDF = fullDF.append(pdtestdata, ignore_index = True)
del pdtestdata



pdtestdata = pd.read_csv('jun2.csv', delimiter=',')
pdtestdata = pdtestdata.drop(pdtestdata.columns[0], axis=1) # Remove ID
#print(pdtestdata)

if (toAvg):
    pdtestdata = ((pdtestdata + pdtestdata.shift(-1) + pdtestdata.shift(-2) + pdtestdata.shift(-3) + pdtestdata.shift(-4)) / 5)[::5]

if (toReshape):
    pdtestdata = pd.DataFrame(np.reshape(pdtestdata.values,(300,240)),  columns=list(range(240)))

pdtestdata = pdtestdata.reset_index(drop=True)
pdtestdata[240]='BusDriver'
#print(pdtestdata)
fullDF = fullDF.append(pdtestdata, ignore_index = True)
del pdtestdata



pdtestdata = pd.read_csv('jun3.csv', delimiter=',')
pdtestdata = pdtestdata.drop(pdtestdata.columns[0], axis=1) # Remove ID
#print(pdtestdata)

if (toAvg):
    pdtestdata = ((pdtestdata + pdtestdata.shift(-1) + pdtestdata.shift(-2) + pdtestdata.shift(-3) + pdtestdata.shift(-4)) / 5)[::5]

if (toReshape):
    pdtestdata = pd.DataFrame(np.reshape(pdtestdata.values,(300,240)),  columns=list(range(240)))

pdtestdata = pdtestdata.reset_index(drop=True)
pdtestdata[240]='FrontBack'
#print(pdtestdata)
fullDF = fullDF.append(pdtestdata, ignore_index = True)
del pdtestdata



pdtestdata = pd.read_csv('jun4.csv', delimiter=',')
pdtestdata = pdtestdata.drop(pdtestdata.columns[0], axis=1) # Remove ID
#print(pdtestdata)

if (toAvg):
    pdtestdata = ((pdtestdata + pdtestdata.shift(-1) + pdtestdata.shift(-2) + pdtestdata.shift(-3) + pdtestdata.shift(-4)) / 5)[::5]

if (toReshape):
    pdtestdata = pd.DataFrame(np.reshape(pdtestdata.values,(300,240)),  columns=list(range(240)))

pdtestdata = pdtestdata.reset_index(drop=True)
pdtestdata[240]='SideStep'
#print(pdtestdata)
fullDF = fullDF.append(pdtestdata, ignore_index = True)
del pdtestdata



pdtestdata = pd.read_csv('jun5.csv', delimiter=',')
pdtestdata = pdtestdata.drop(pdtestdata.columns[0], axis=1) # Remove ID
#print(pdtestdata)

if (toAvg):
    pdtestdata = ((pdtestdata + pdtestdata.shift(-1) + pdtestdata.shift(-2) + pdtestdata.shift(-3) + pdtestdata.shift(-4)) / 5)[::5]

if (toReshape):
    pdtestdata = pd.DataFrame(np.reshape(pdtestdata.values,(300,240)),  columns=list(range(240)))

pdtestdata = pdtestdata.reset_index(drop=True)
pdtestdata[240]='Jumping'
#print(pdtestdata)
fullDF = fullDF.append(pdtestdata, ignore_index = True)
del pdtestdata




print(fullDF)

fullDF.to_csv('processed_data.csv', sep=',')
