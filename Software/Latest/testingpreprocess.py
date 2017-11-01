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
reshapeBy = 10

fullDF = pd.DataFrame(columns=list(range(121)))



pdtestdata = pd.read_csv('nic0.csv', delimiter=',')
pdtestdata = pdtestdata.drop(pdtestdata.columns[0], axis=1) # Remove ID
#print(pdtestdata)

if (toAvg):
    pdtestdata = ((pdtestdata + pdtestdata.shift(-1) + pdtestdata.shift(-2) + pdtestdata.shift(-3) + pdtestdata.shift(-4)) / 5)[::5]

if (toReshape):
    pdtestdata = pd.DataFrame(np.reshape(pdtestdata.values,(600,120)),  columns=list(range(120)))

pdtestdata = pdtestdata.reset_index(drop=True)
pdtestdata[120]='Standing'
#print(pdtestdata)
fullDF = fullDF.append(pdtestdata, ignore_index = True)
del pdtestdata



pdtestdata = pd.read_csv('nic1.csv', delimiter=',')
pdtestdata = pdtestdata.drop(pdtestdata.columns[0], axis=1) # Remove ID
#print(pdtestdata)

if (toAvg):
    pdtestdata = ((pdtestdata + pdtestdata.shift(-1) + pdtestdata.shift(-2) + pdtestdata.shift(-3) + pdtestdata.shift(-4)) / 5)[::5]

if (toReshape):
    pdtestdata = pd.DataFrame(np.reshape(pdtestdata.values,(600,120)),  columns=list(range(120)))

pdtestdata = pdtestdata.reset_index(drop=True)
pdtestdata[120]='WaveHands'
#print(pdtestdata)
fullDF = fullDF.append(pdtestdata, ignore_index = True)
del pdtestdata



pdtestdata = pd.read_csv('nic2.csv', delimiter=',')
pdtestdata = pdtestdata.drop(pdtestdata.columns[0], axis=1) # Remove ID
#print(pdtestdata)

if (toAvg):
    pdtestdata = ((pdtestdata + pdtestdata.shift(-1) + pdtestdata.shift(-2) + pdtestdata.shift(-3) + pdtestdata.shift(-4)) / 5)[::5]

if (toReshape):
    pdtestdata = pd.DataFrame(np.reshape(pdtestdata.values,(600,120)),  columns=list(range(120)))

pdtestdata = pdtestdata.reset_index(drop=True)
pdtestdata[120]='BusDriver'
#print(pdtestdata)
fullDF = fullDF.append(pdtestdata, ignore_index = True)
del pdtestdata



pdtestdata = pd.read_csv('nic3.csv', delimiter=',')
pdtestdata = pdtestdata.drop(pdtestdata.columns[0], axis=1) # Remove ID
#print(pdtestdata)

if (toAvg):
    pdtestdata = ((pdtestdata + pdtestdata.shift(-1) + pdtestdata.shift(-2) + pdtestdata.shift(-3) + pdtestdata.shift(-4)) / 5)[::5]

if (toReshape):
    pdtestdata = pd.DataFrame(np.reshape(pdtestdata.values,(600,120)),  columns=list(range(120)))

pdtestdata = pdtestdata.reset_index(drop=True)
pdtestdata[120]='FrontBack'
#print(pdtestdata)
fullDF = fullDF.append(pdtestdata, ignore_index = True)
del pdtestdata



pdtestdata = pd.read_csv('nic4.csv', delimiter=',')
pdtestdata = pdtestdata.drop(pdtestdata.columns[0], axis=1) # Remove ID
#print(pdtestdata)

if (toAvg):
    pdtestdata = ((pdtestdata + pdtestdata.shift(-1) + pdtestdata.shift(-2) + pdtestdata.shift(-3) + pdtestdata.shift(-4)) / 5)[::5]

if (toReshape):
    pdtestdata = pd.DataFrame(np.reshape(pdtestdata.values,(600,120)),  columns=list(range(120)))

pdtestdata = pdtestdata.reset_index(drop=True)
pdtestdata[120]='SideStep'
#print(pdtestdata)
fullDF = fullDF.append(pdtestdata, ignore_index = True)
del pdtestdata



pdtestdata = pd.read_csv('nic5.csv', delimiter=',')
pdtestdata = pdtestdata.drop(pdtestdata.columns[0], axis=1) # Remove ID
#print(pdtestdata)

if (toAvg):
    pdtestdata = ((pdtestdata + pdtestdata.shift(-1) + pdtestdata.shift(-2) + pdtestdata.shift(-3) + pdtestdata.shift(-4)) / 5)[::5]

if (toReshape):
    pdtestdata = pd.DataFrame(np.reshape(pdtestdata.values,(600,120)),  columns=list(range(120)))

pdtestdata = pdtestdata.reset_index(drop=True)
pdtestdata[120]='Jumping'
#print(pdtestdata)
fullDF = fullDF.append(pdtestdata, ignore_index = True)
del pdtestdata



pdtestdata = pd.read_csv('Raph0.csv', delimiter=',')
pdtestdata = pdtestdata.drop(pdtestdata.columns[0], axis=1) # Remove ID
#print(pdtestdata)

if (toAvg):
    pdtestdata = ((pdtestdata + pdtestdata.shift(-1) + pdtestdata.shift(-2) + pdtestdata.shift(-3) + pdtestdata.shift(-4)) / 5)[::5]

if (toReshape):
    pdtestdata = pd.DataFrame(np.reshape(pdtestdata.values,(600,120)),  columns=list(range(120)))

pdtestdata = pdtestdata.reset_index(drop=True)
pdtestdata[120]='Standing'
#print(pdtestdata)
fullDF = fullDF.append(pdtestdata, ignore_index = True)
del pdtestdata



pdtestdata = pd.read_csv('Raph1.csv', delimiter=',')
pdtestdata = pdtestdata.drop(pdtestdata.columns[0], axis=1) # Remove ID
#print(pdtestdata)

if (toAvg):
    pdtestdata = ((pdtestdata + pdtestdata.shift(-1) + pdtestdata.shift(-2) + pdtestdata.shift(-3) + pdtestdata.shift(-4)) / 5)[::5]

if (toReshape):
    pdtestdata = pd.DataFrame(np.reshape(pdtestdata.values,(600,120)),  columns=list(range(120)))

pdtestdata = pdtestdata.reset_index(drop=True)
pdtestdata[120]='WaveHands'
#print(pdtestdata)
fullDF = fullDF.append(pdtestdata, ignore_index = True)
del pdtestdata



pdtestdata = pd.read_csv('Raph2.csv', delimiter=',')
pdtestdata = pdtestdata.drop(pdtestdata.columns[0], axis=1) # Remove ID
#print(pdtestdata)

if (toAvg):
    pdtestdata = ((pdtestdata + pdtestdata.shift(-1) + pdtestdata.shift(-2) + pdtestdata.shift(-3) + pdtestdata.shift(-4)) / 5)[::5]

if (toReshape):
    pdtestdata = pd.DataFrame(np.reshape(pdtestdata.values,(600,120)),  columns=list(range(120)))

pdtestdata = pdtestdata.reset_index(drop=True)
pdtestdata[120]='BusDriver'
#print(pdtestdata)
fullDF = fullDF.append(pdtestdata, ignore_index = True)
del pdtestdata



pdtestdata = pd.read_csv('Raph3.csv', delimiter=',')
pdtestdata = pdtestdata.drop(pdtestdata.columns[0], axis=1) # Remove ID
#print(pdtestdata)

if (toAvg):
    pdtestdata = ((pdtestdata + pdtestdata.shift(-1) + pdtestdata.shift(-2) + pdtestdata.shift(-3) + pdtestdata.shift(-4)) / 5)[::5]

if (toReshape):
    pdtestdata = pd.DataFrame(np.reshape(pdtestdata.values,(600,120)),  columns=list(range(120)))

pdtestdata = pdtestdata.reset_index(drop=True)
pdtestdata[120]='FrontBack'
#print(pdtestdata)
fullDF = fullDF.append(pdtestdata, ignore_index = True)
del pdtestdata



pdtestdata = pd.read_csv('Raph4.csv', delimiter=',')
pdtestdata = pdtestdata.drop(pdtestdata.columns[0], axis=1) # Remove ID
#print(pdtestdata)

if (toAvg):
    pdtestdata = ((pdtestdata + pdtestdata.shift(-1) + pdtestdata.shift(-2) + pdtestdata.shift(-3) + pdtestdata.shift(-4)) / 5)[::5]

if (toReshape):
    pdtestdata = pd.DataFrame(np.reshape(pdtestdata.values,(600,120)),  columns=list(range(120)))

pdtestdata = pdtestdata.reset_index(drop=True)
pdtestdata[120]='SideStep'
#print(pdtestdata)
fullDF = fullDF.append(pdtestdata, ignore_index = True)
del pdtestdata



pdtestdata = pd.read_csv('Raph5.csv', delimiter=',')
pdtestdata = pdtestdata.drop(pdtestdata.columns[0], axis=1) # Remove ID
#print(pdtestdata)

if (toAvg):
    pdtestdata = ((pdtestdata + pdtestdata.shift(-1) + pdtestdata.shift(-2) + pdtestdata.shift(-3) + pdtestdata.shift(-4)) / 5)[::5]

if (toReshape):
    pdtestdata = pd.DataFrame(np.reshape(pdtestdata.values,(600,120)),  columns=list(range(120)))

pdtestdata = pdtestdata.reset_index(drop=True)
pdtestdata[120]='Jumping'
#print(pdtestdata)
fullDF = fullDF.append(pdtestdata, ignore_index = True)
del pdtestdata




print(fullDF)

fullDF.to_csv('processed_data.csv', sep=',')
