# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 16:39:56 2017

@author: diary
"""
import pandas as pd
import numpy as np
#import csv
#from sklearn import preprocessing

# Config.ini
toAvg = 0
avgBy = 5
toReshape = 1
reshapeBy = 40 # Set number of inputs per sample for Machine Learning

fullDF = pd.DataFrame(columns=list(range(int(reshapeBy*12)+1)))



pdtestdata = pd.read_csv('Raw Data\\nic0.csv', delimiter=',')
pdtestdata = pdtestdata.drop(pdtestdata.columns[0], axis=1) # Remove ID

#print(pdtestdata)

if (toAvg):
    pdtestdata = ((pdtestdata + pdtestdata.shift(-1) + pdtestdata.shift(-2) + pdtestdata.shift(-3) + pdtestdata.shift(-4)) / 5)[::5]

if (toReshape):
    rowsLeft=(pdtestdata.shape[0])/int(reshapeBy) #gives number of row count after reshape
    pdtestdata = pd.DataFrame(np.reshape(pdtestdata.values,(int(rowsLeft),int(reshapeBy*12))),  columns=list(range(int(reshapeBy*12))))

pdtestdata = pdtestdata.reset_index(drop=True)
pdtestdata[int(reshapeBy*12)]='Standing'
#print(pdtestdata)
fullDF = fullDF.append(pdtestdata, ignore_index = True)
del pdtestdata



pdtestdata = pd.read_csv('Raw Data\\nic1.csv', delimiter=',')
pdtestdata = pdtestdata.drop(pdtestdata.columns[0], axis=1) # Remove ID
#print(pdtestdata)

if (toAvg):
    pdtestdata = ((pdtestdata + pdtestdata.shift(-1) + pdtestdata.shift(-2) + pdtestdata.shift(-3) + pdtestdata.shift(-4)) / 5)[::5]

if (toReshape):
    rowsLeft=(pdtestdata.shape[0])/int(reshapeBy) #gives number of row count after reshape
    pdtestdata = pd.DataFrame(np.reshape(pdtestdata.values,(int(rowsLeft),int(reshapeBy*12))),  columns=list(range(int(reshapeBy*12))))

pdtestdata = pdtestdata.reset_index(drop=True)
pdtestdata[int(reshapeBy*12)]='WaveHands'
#print(pdtestdata)
fullDF = fullDF.append(pdtestdata, ignore_index = True)
del pdtestdata



pdtestdata = pd.read_csv('Raw Data\\nic2.csv', delimiter=',')
pdtestdata = pdtestdata.drop(pdtestdata.columns[0], axis=1) # Remove ID
#print(pdtestdata)

if (toAvg):
    pdtestdata = ((pdtestdata + pdtestdata.shift(-1) + pdtestdata.shift(-2) + pdtestdata.shift(-3) + pdtestdata.shift(-4)) / 5)[::5]

if (toReshape):
    rowsLeft=(pdtestdata.shape[0])/int(reshapeBy) #gives number of row count after reshape
    pdtestdata = pd.DataFrame(np.reshape(pdtestdata.values,(int(rowsLeft),int(reshapeBy*12))),  columns=list(range(int(reshapeBy*12))))

pdtestdata = pdtestdata.reset_index(drop=True)
pdtestdata[int(reshapeBy*12)]='BusDriver'
#print(pdtestdata)
fullDF = fullDF.append(pdtestdata, ignore_index = True)
del pdtestdata



pdtestdata = pd.read_csv('Raw Data\\nic3.csv', delimiter=',')
pdtestdata = pdtestdata.drop(pdtestdata.columns[0], axis=1) # Remove ID
#print(pdtestdata)

if (toAvg):
    pdtestdata = ((pdtestdata + pdtestdata.shift(-1) + pdtestdata.shift(-2) + pdtestdata.shift(-3) + pdtestdata.shift(-4)) / 5)[::5]

if (toReshape):
    rowsLeft=(pdtestdata.shape[0])/int(reshapeBy) #gives number of row count after reshape
    pdtestdata = pd.DataFrame(np.reshape(pdtestdata.values,(int(rowsLeft),int(reshapeBy*12))),  columns=list(range(int(reshapeBy*12))))

pdtestdata = pdtestdata.reset_index(drop=True)
pdtestdata[int(reshapeBy*12)]='FrontBack'
#print(pdtestdata)
fullDF = fullDF.append(pdtestdata, ignore_index = True)
del pdtestdata



pdtestdata = pd.read_csv('Raw Data\\nic4.csv', delimiter=',')
pdtestdata = pdtestdata.drop(pdtestdata.columns[0], axis=1) # Remove ID
#print(pdtestdata)

if (toAvg):
    pdtestdata = ((pdtestdata + pdtestdata.shift(-1) + pdtestdata.shift(-2) + pdtestdata.shift(-3) + pdtestdata.shift(-4)) / 5)[::5]

if (toReshape):
    rowsLeft=(pdtestdata.shape[0])/int(reshapeBy) #gives number of row count after reshape
    pdtestdata = pd.DataFrame(np.reshape(pdtestdata.values,(int(rowsLeft),int(reshapeBy*12))),  columns=list(range(int(reshapeBy*12))))

pdtestdata = pdtestdata.reset_index(drop=True)
pdtestdata[int(reshapeBy*12)]='SideStep'
#print(pdtestdata)
fullDF = fullDF.append(pdtestdata, ignore_index = True)
del pdtestdata



pdtestdata = pd.read_csv('Raw Data\\nic5.csv', delimiter=',')
pdtestdata = pdtestdata.drop(pdtestdata.columns[0], axis=1) # Remove ID
#print(pdtestdata)

if (toAvg):
    pdtestdata = ((pdtestdata + pdtestdata.shift(-1) + pdtestdata.shift(-2) + pdtestdata.shift(-3) + pdtestdata.shift(-4)) / 5)[::5]

if (toReshape):
    rowsLeft=(pdtestdata.shape[0])/int(reshapeBy) #gives number of row count after reshape
    pdtestdata = pd.DataFrame(np.reshape(pdtestdata.values,(int(rowsLeft),int(reshapeBy*12))),  columns=list(range(int(reshapeBy*12))))
##Encode output variable
le = preprocessing.LabelEncoder()
le.fit(['standing', 'wavehands', 'busdriver', 'frontback', 'sidestep', 'jumping', 'jumpingjack', 'turnclap', 'squatturnclap', 'windowcleaning', 'windowcleaner360', 'logout'])
print(list(le.classes_))

pdtestdata = pdtestdata.reset_index(drop=True)
pdtestdata[int(reshapeBy*12)]='Jumping'
#print(pdtestdata)
fullDF = fullDF.append(pdtestdata, ignore_index = True)
del pdtestdata



pdtestdata = pd.read_csv('Raw Data\\Raph0.csv', delimiter=',')
pdtestdata = pdtestdata.drop(pdtestdata.columns[0], axis=1) # Remove ID
#print(pdtestdata)

if (toAvg):
    pdtestdata = ((pdtestdata + pdtestdata.shift(-1) + pdtestdata.shift(-2) + pdtestdata.shift(-3) + pdtestdata.shift(-4)) / 5)[::5]

if (toReshape):
    rowsLeft=(pdtestdata.shape[0])/int(reshapeBy) #gives number of row count after reshape
    pdtestdata = pd.DataFrame(np.reshape(pdtestdata.values,(int(rowsLeft),int(reshapeBy*12))),  columns=list(range(int(reshapeBy*12))))

pdtestdata = pdtestdata.reset_index(drop=True)
pdtestdata[int(reshapeBy*12)]='Standing'
#print(pdtestdata)
fullDF = fullDF.append(pdtestdata, ignore_index = True)
del pdtestdata



pdtestdata = pd.read_csv('Raw Data\\raph0_2.csv', delimiter=',')
pdtestdata = pdtestdata.drop(pdtestdata.columns[0], axis=1) # Remove ID
#print(pdtestdata)

if (toAvg):
    pdtestdata = ((pdtestdata + pdtestdata.shift(-1) + pdtestdata.shift(-2) + pdtestdata.shift(-3) + pdtestdata.shift(-4)) / 5)[::5]

if (toReshape):
    rowsLeft=(pdtestdata.shape[0])/int(reshapeBy) #gives number of row count after reshape
    pdtestdata = pd.DataFrame(np.reshape(pdtestdata.values,(int(rowsLeft),int(reshapeBy*12))),  columns=list(range(int(reshapeBy*12))))

pdtestdata = pdtestdata.reset_index(drop=True)
pdtestdata[int(reshapeBy*12)]='Standing'
#print(pdtestdata)
fullDF = fullDF.append(pdtestdata, ignore_index = True)
del pdtestdata



pdtestdata = pd.read_csv('Raw Data\\Raph1.csv', delimiter=',')
pdtestdata = pdtestdata.drop(pdtestdata.columns[0], axis=1) # Remove ID
#print(pdtestdata)

if (toAvg):
    pdtestdata = ((pdtestdata + pdtestdata.shift(-1) + pdtestdata.shift(-2) + pdtestdata.shift(-3) + pdtestdata.shift(-4)) / 5)[::5]

if (toReshape):
    rowsLeft=(pdtestdata.shape[0])/int(reshapeBy) #gives number of row count after reshape
    pdtestdata = pd.DataFrame(np.reshape(pdtestdata.values,(int(rowsLeft),int(reshapeBy*12))),  columns=list(range(int(reshapeBy*12))))

pdtestdata = pdtestdata.reset_index(drop=True)
pdtestdata[int(reshapeBy*12)]='WaveHands'
#print(pdtestdata)
fullDF = fullDF.append(pdtestdata, ignore_index = True)
del pdtestdata



pdtestdata = pd.read_csv('Raw Data\\Raph2.csv', delimiter=',')
pdtestdata = pdtestdata.drop(pdtestdata.columns[0], axis=1) # Remove ID
#print(pdtestdata)

if (toAvg):
    pdtestdata = ((pdtestdata + pdtestdata.shift(-1) + pdtestdata.shift(-2) + pdtestdata.shift(-3) + pdtestdata.shift(-4)) / 5)[::5]

if (toReshape):
    rowsLeft=(pdtestdata.shape[0])/int(reshapeBy) #gives number of row count after reshape
    pdtestdata = pd.DataFrame(np.reshape(pdtestdata.values,(int(rowsLeft),int(reshapeBy*12))),  columns=list(range(int(reshapeBy*12))))

pdtestdata = pdtestdata.reset_index(drop=True)
pdtestdata[int(reshapeBy*12)]='BusDriver'
#print(pdtestdata)
fullDF = fullDF.append(pdtestdata, ignore_index = True)
del pdtestdata



pdtestdata = pd.read_csv('Raw Data\\Raph3.csv', delimiter=',')
pdtestdata = pdtestdata.drop(pdtestdata.columns[0], axis=1) # Remove ID
#print(pdtestdata)

if (toAvg):
    pdtestdata = ((pdtestdata + pdtestdata.shift(-1) + pdtestdata.shift(-2) + pdtestdata.shift(-3) + pdtestdata.shift(-4)) / 5)[::5]

if (toReshape):
    rowsLeft=(pdtestdata.shape[0])/int(reshapeBy) #gives number of row count after reshape
    pdtestdata = pd.DataFrame(np.reshape(pdtestdata.values,(int(rowsLeft),int(reshapeBy*12))),  columns=list(range(int(reshapeBy*12))))

pdtestdata = pdtestdata.reset_index(drop=True)
pdtestdata[int(reshapeBy*12)]='FrontBack'
#print(pdtestdata)
fullDF = fullDF.append(pdtestdata, ignore_index = True)
del pdtestdata



pdtestdata = pd.read_csv('Raw Data\\raph3_2.csv', delimiter=',')
pdtestdata = pdtestdata.drop(pdtestdata.columns[0], axis=1) # Remove ID
#print(pdtestdata)

if (toAvg):
    pdtestdata = ((pdtestdata + pdtestdata.shift(-1) + pdtestdata.shift(-2) + pdtestdata.shift(-3) + pdtestdata.shift(-4)) / 5)[::5]

if (toReshape):
    rowsLeft=(pdtestdata.shape[0])/int(reshapeBy) #gives number of row count after reshape
    pdtestdata = pd.DataFrame(np.reshape(pdtestdata.values,(int(rowsLeft),int(reshapeBy*12))),  columns=list(range(int(reshapeBy*12))))

pdtestdata = pdtestdata.reset_index(drop=True)
pdtestdata[int(reshapeBy*12)]='FrontBack'
#print(pdtestdata)
fullDF = fullDF.append(pdtestdata, ignore_index = True)
del pdtestdata



pdtestdata = pd.read_csv('Raw Data\\Raph4.csv', delimiter=',')
pdtestdata = pdtestdata.drop(pdtestdata.columns[0], axis=1) # Remove ID
#print(pdtestdata)

if (toAvg):
    pdtestdata = ((pdtestdata + pdtestdata.shift(-1) + pdtestdata.shift(-2) + pdtestdata.shift(-3) + pdtestdata.shift(-4)) / 5)[::5]

if (toReshape):
    rowsLeft=(pdtestdata.shape[0])/int(reshapeBy) #gives number of row count after reshape
    pdtestdata = pd.DataFrame(np.reshape(pdtestdata.values,(int(rowsLeft),int(reshapeBy*12))),  columns=list(range(int(reshapeBy*12))))

pdtestdata = pdtestdata.reset_index(drop=True)
pdtestdata[int(reshapeBy*12)]='SideStep'
#print(pdtestdata)
fullDF = fullDF.append(pdtestdata, ignore_index = True)
del pdtestdata



pdtestdata = pd.read_csv('Raw Data\\raph4_2.csv', delimiter=',')
pdtestdata = pdtestdata.drop(pdtestdata.columns[0], axis=1) # Remove ID
#print(pdtestdata)

if (toAvg):
    pdtestdata = ((pdtestdata + pdtestdata.shift(-1) + pdtestdata.shift(-2) + pdtestdata.shift(-3) + pdtestdata.shift(-4)) / 5)[::5]

if (toReshape):
    rowsLeft=(pdtestdata.shape[0])/int(reshapeBy) #gives number of row count after reshape
    pdtestdata = pd.DataFrame(np.reshape(pdtestdata.values,(int(rowsLeft),int(reshapeBy*12))),  columns=list(range(int(reshapeBy*12))))

pdtestdata = pdtestdata.reset_index(drop=True)
pdtestdata[int(reshapeBy*12)]='SideStep'
#print(pdtestdata)
fullDF = fullDF.append(pdtestdata, ignore_index = True)
del pdtestdata



pdtestdata = pd.read_csv('Raw Data\\Raph5.csv', delimiter=',')
pdtestdata = pdtestdata.drop(pdtestdata.columns[0], axis=1) # Remove ID
#print(pdtestdata)

if (toAvg):
    pdtestdata = ((pdtestdata + pdtestdata.shift(-1) + pdtestdata.shift(-2) + pdtestdata.shift(-3) + pdtestdata.shift(-4)) / 5)[::5]

if (toReshape):
    rowsLeft=(pdtestdata.shape[0])/int(reshapeBy) #gives number of row count after reshape
    pdtestdata = pd.DataFrame(np.reshape(pdtestdata.values,(int(rowsLeft),int(reshapeBy*12))),  columns=list(range(int(reshapeBy*12))))

pdtestdata = pdtestdata.reset_index(drop=True)
pdtestdata[int(reshapeBy*12)]='Jumping'
#print(pdtestdata)
fullDF = fullDF.append(pdtestdata, ignore_index = True)
del pdtestdata



pdtestdata = pd.read_csv('Raw Data\\manish0.csv', delimiter=',')
pdtestdata = pdtestdata.drop(pdtestdata.columns[0], axis=1) # Remove ID
#print(pdtestdata)

if (toAvg):
    pdtestdata = ((pdtestdata + pdtestdata.shift(-1) + pdtestdata.shift(-2) + pdtestdata.shift(-3) + pdtestdata.shift(-4)) / 5)[::5]

if (toReshape):
    rowsLeft=(pdtestdata.shape[0])/int(reshapeBy) #gives number of row count after reshape
    pdtestdata = pd.DataFrame(np.reshape(pdtestdata.values,(int(rowsLeft),int(reshapeBy*12))),  columns=list(range(int(reshapeBy*12))))

pdtestdata = pdtestdata.reset_index(drop=True)
pdtestdata[int(reshapeBy*12)]='Standing'
#print(pdtestdata)
fullDF = fullDF.append(pdtestdata, ignore_index = True)
del pdtestdata



pdtestdata = pd.read_csv('Raw Data\\manish1.csv', delimiter=',')
pdtestdata = pdtestdata.drop(pdtestdata.columns[0], axis=1) # Remove ID
#print(pdtestdata)

if (toAvg):
    pdtestdata = ((pdtestdata + pdtestdata.shift(-1) + pdtestdata.shift(-2) + pdtestdata.shift(-3) + pdtestdata.shift(-4)) / 5)[::5]

if (toReshape):
    rowsLeft=(pdtestdata.shape[0])/int(reshapeBy) #gives number of row count after reshape
    pdtestdata = pd.DataFrame(np.reshape(pdtestdata.values,(int(rowsLeft),int(reshapeBy*12))),  columns=list(range(int(reshapeBy*12))))

pdtestdata = pdtestdata.reset_index(drop=True)
pdtestdata[int(reshapeBy*12)]='WaveHands'
#print(pdtestdata)
fullDF = fullDF.append(pdtestdata, ignore_index = True)
del pdtestdata



pdtestdata = pd.read_csv('Raw Data\\manish2.csv', delimiter=',')
pdtestdata = pdtestdata.drop(pdtestdata.columns[0], axis=1) # Remove ID
#print(pdtestdata)

if (toAvg):
    pdtestdata = ((pdtestdata + pdtestdata.shift(-1) + pdtestdata.shift(-2) + pdtestdata.shift(-3) + pdtestdata.shift(-4)) / 5)[::5]

if (toReshape):
    rowsLeft=(pdtestdata.shape[0])/int(reshapeBy) #gives number of row count after reshape
    pdtestdata = pd.DataFrame(np.reshape(pdtestdata.values,(int(rowsLeft),int(reshapeBy*12))),  columns=list(range(int(reshapeBy*12))))

pdtestdata = pdtestdata.reset_index(drop=True)
pdtestdata[int(reshapeBy*12)]='BusDriver'
#print(pdtestdata)
fullDF = fullDF.append(pdtestdata, ignore_index = True)
del pdtestdata



pdtestdata = pd.read_csv('Raw Data\\manish3.csv', delimiter=',')
pdtestdata = pdtestdata.drop(pdtestdata.columns[0], axis=1) # Remove ID
#print(pdtestdata)

if (toAvg):
    pdtestdata = ((pdtestdata + pdtestdata.shift(-1) + pdtestdata.shift(-2) + pdtestdata.shift(-3) + pdtestdata.shift(-4)) / 5)[::5]

if (toReshape):
    rowsLeft=(pdtestdata.shape[0])/int(reshapeBy) #gives number of row count after reshape
    pdtestdata = pd.DataFrame(np.reshape(pdtestdata.values,(int(rowsLeft),int(reshapeBy*12))),  columns=list(range(int(reshapeBy*12))))

pdtestdata = pdtestdata.reset_index(drop=True)
pdtestdata[int(reshapeBy*12)]='FrontBack'
#print(pdtestdata)
fullDF = fullDF.append(pdtestdata, ignore_index = True)
del pdtestdata



pdtestdata = pd.read_csv('Raw Data\\manish4.csv', delimiter=',')
pdtestdata = pdtestdata.drop(pdtestdata.columns[0], axis=1) # Remove ID
#print(pdtestdata)

if (toAvg):
    pdtestdata = ((pdtestdata + pdtestdata.shift(-1) + pdtestdata.shift(-2) + pdtestdata.shift(-3) + pdtestdata.shift(-4)) / 5)[::5]

if (toReshape):
    rowsLeft=(pdtestdata.shape[0])/int(reshapeBy) #gives number of row count after reshape
    pdtestdata = pd.DataFrame(np.reshape(pdtestdata.values,(int(rowsLeft),int(reshapeBy*12))),  columns=list(range(int(reshapeBy*12))))

pdtestdata = pdtestdata.reset_index(drop=True)
pdtestdata[int(reshapeBy*12)]='SideStep'
#print(pdtestdata)
fullDF = fullDF.append(pdtestdata, ignore_index = True)
del pdtestdata



pdtestdata = pd.read_csv('Raw Data\\manish5.csv', delimiter=',')
pdtestdata = pdtestdata.drop(pdtestdata.columns[0], axis=1) # Remove ID
#print(pdtestdata)

if (toAvg):
    pdtestdata = ((pdtestdata + pdtestdata.shift(-1) + pdtestdata.shift(-2) + pdtestdata.shift(-3) + pdtestdata.shift(-4)) / 5)[::5]

if (toReshape):
    rowsLeft=(pdtestdata.shape[0])/int(reshapeBy) #gives number of row count after reshape
    pdtestdata = pd.DataFrame(np.reshape(pdtestdata.values,(int(rowsLeft),int(reshapeBy*12))),  columns=list(range(int(reshapeBy*12))))

pdtestdata = pdtestdata.reset_index(drop=True)
pdtestdata[int(reshapeBy*12)]='Jumping'
#print(pdtestdata)
fullDF = fullDF.append(pdtestdata, ignore_index = True)
del pdtestdata



pdtestdata = pd.read_csv('Raw Data\\jun0.csv', delimiter=',')
pdtestdata = pdtestdata.drop(pdtestdata.columns[0], axis=1) # Remove ID
#print(pdtestdata)

if (toAvg):
    pdtestdata = ((pdtestdata + pdtestdata.shift(-1) + pdtestdata.shift(-2) + pdtestdata.shift(-3) + pdtestdata.shift(-4)) / 5)[::5]

if (toReshape):
    rowsLeft=(pdtestdata.shape[0])/int(reshapeBy) #gives number of row count after reshape
    pdtestdata = pd.DataFrame(np.reshape(pdtestdata.values,(int(rowsLeft),int(reshapeBy*12))),  columns=list(range(int(reshapeBy*12))))

pdtestdata = pdtestdata.reset_index(drop=True)
pdtestdata[int(reshapeBy*12)]='Standing'
#print(pdtestdata)
fullDF = fullDF.append(pdtestdata, ignore_index = True)
del pdtestdata



pdtestdata = pd.read_csv('Raw Data\\jun1.csv', delimiter=',')
pdtestdata = pdtestdata.drop(pdtestdata.columns[0], axis=1) # Remove ID
#print(pdtestdata)

if (toAvg):
    pdtestdata = ((pdtestdata + pdtestdata.shift(-1) + pdtestdata.shift(-2) + pdtestdata.shift(-3) + pdtestdata.shift(-4)) / 5)[::5]

if (toReshape):
    rowsLeft=(pdtestdata.shape[0])/int(reshapeBy) #gives number of row count after reshape
    pdtestdata = pd.DataFrame(np.reshape(pdtestdata.values,(int(rowsLeft),int(reshapeBy*12))),  columns=list(range(int(reshapeBy*12))))

pdtestdata = pdtestdata.reset_index(drop=True)
pdtestdata[int(reshapeBy*12)]='WaveHands'
#print(pdtestdata)
fullDF = fullDF.append(pdtestdata, ignore_index = True)
del pdtestdata



pdtestdata = pd.read_csv('Raw Data\\jun2.csv', delimiter=',')
pdtestdata = pdtestdata.drop(pdtestdata.columns[0], axis=1) # Remove ID
#print(pdtestdata)

if (toAvg):
    pdtestdata = ((pdtestdata + pdtestdata.shift(-1) + pdtestdata.shift(-2) + pdtestdata.shift(-3) + pdtestdata.shift(-4)) / 5)[::5]

if (toReshape):
    rowsLeft=(pdtestdata.shape[0])/int(reshapeBy) #gives number of row count after reshape
    pdtestdata = pd.DataFrame(np.reshape(pdtestdata.values,(int(rowsLeft),int(reshapeBy*12))),  columns=list(range(int(reshapeBy*12))))

pdtestdata = pdtestdata.reset_index(drop=True)
pdtestdata[int(reshapeBy*12)]='BusDriver'
#print(pdtestdata)
fullDF = fullDF.append(pdtestdata, ignore_index = True)
del pdtestdata



pdtestdata = pd.read_csv('Raw Data\\jun3.csv', delimiter=',')
pdtestdata = pdtestdata.drop(pdtestdata.columns[0], axis=1) # Remove ID
#print(pdtestdata)

if (toAvg):
    pdtestdata = ((pdtestdata + pdtestdata.shift(-1) + pdtestdata.shift(-2) + pdtestdata.shift(-3) + pdtestdata.shift(-4)) / 5)[::5]

if (toReshape):
    rowsLeft=(pdtestdata.shape[0])/int(reshapeBy) #gives number of row count after reshape
    pdtestdata = pd.DataFrame(np.reshape(pdtestdata.values,(int(rowsLeft),int(reshapeBy*12))),  columns=list(range(int(reshapeBy*12))))

pdtestdata = pdtestdata.reset_index(drop=True)
pdtestdata[int(reshapeBy*12)]='FrontBack'
#print(pdtestdata)
fullDF = fullDF.append(pdtestdata, ignore_index = True)
del pdtestdata



pdtestdata = pd.read_csv('Raw Data\\jun4.csv', delimiter=',')
pdtestdata = pdtestdata.drop(pdtestdata.columns[0], axis=1) # Remove ID
#print(pdtestdata)

if (toAvg):
    pdtestdata = ((pdtestdata + pdtestdata.shift(-1) + pdtestdata.shift(-2) + pdtestdata.shift(-3) + pdtestdata.shift(-4)) / 5)[::5]

if (toReshape):
    rowsLeft=(pdtestdata.shape[0])/int(reshapeBy) #gives number of row count after reshape
    pdtestdata = pd.DataFrame(np.reshape(pdtestdata.values,(int(rowsLeft),int(reshapeBy*12))),  columns=list(range(int(reshapeBy*12))))

pdtestdata = pdtestdata.reset_index(drop=True)
pdtestdata[int(reshapeBy*12)]='SideStep'
#print(pdtestdata)
fullDF = fullDF.append(pdtestdata, ignore_index = True)
del pdtestdata



pdtestdata = pd.read_csv('Raw Data\\jun5.csv', delimiter=',')
pdtestdata = pdtestdata.drop(pdtestdata.columns[0], axis=1) # Remove ID
#print(pdtestdata)

if (toAvg):
    pdtestdata = ((pdtestdata + pdtestdata.shift(-1) + pdtestdata.shift(-2) + pdtestdata.shift(-3) + pdtestdata.shift(-4)) / 5)[::5]

if (toReshape):
    rowsLeft=(pdtestdata.shape[0])/int(reshapeBy) #gives number of row count after reshape
    pdtestdata = pd.DataFrame(np.reshape(pdtestdata.values,(int(rowsLeft),int(reshapeBy*12))),  columns=list(range(int(reshapeBy*12))))

pdtestdata = pdtestdata.reset_index(drop=True)
pdtestdata[int(reshapeBy*12)]='Jumping'
#print(pdtestdata)
fullDF = fullDF.append(pdtestdata, ignore_index = True)
del pdtestdata




print(fullDF)

fullDF.to_csv('processed_data.csv', sep=',')
