# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 16:39:56 2017

@author: diary
"""
import pandas as pd
import numpy as np
#import csv
#from sklearn import preprocessing
import os

# Config.ini
toAvg = 0
avgBy = 5
toReshape = 1
reshapeBy = 50 # Set number of inputs per sample for Machine Learning
firstFile = True

# Declare column headers
cols = [list(range(1, (9*reshapeBy)+2))] # 1-480
#fullDF = pd.DataFrame(columns=cols)


#Data pre-processing
from sklearn import preprocessing

##Encode output variable
le = preprocessing.LabelEncoder()
le.fit(['standing', 'wavehands', 'busdriver', 'frontback', 'sidestep', 'jumping', 'jumpingjack', 'turnclap', 'squatturnclap', 'windowcleaning', 'windowcleaner360', 'logout'])
print(list(le.classes_))
#print(le.transform(['standing', 'wavehands', 'busdriver']) )


for filename in os.listdir('RawData'):
    if (firstFile):
        firstFile = False
        pathedFileName = "RawData\\" + filename
        print(pathedFileName)
        pdtestdata = pd.read_csv("RawData\\"+str(filename), delimiter=',')
        pdtestdata = pdtestdata.drop(pdtestdata.columns[0], axis=1) # Remove ID
        fullDF = pdtestdata.reset_index(drop=True)
        del pdtestdata
    else:
        pathedFileName = "RawData\\" + filename
        print(pathedFileName)
        pdtestdata = pd.read_csv("RawData\\"+str(filename), delimiter=',')
        pdtestdata = pdtestdata.drop(pdtestdata.columns[0], axis=1) # Remove ID
        fullDF = pd.concat([fullDF, pdtestdata], axis=0)
        del pdtestdata


print(fullDF)
fullDF.to_csv('processed_data.csv', sep=',')
