# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 16:39:56 2017

@author: diary
"""
import pandas as pd
import numpy as np
import csv
from sklearn import preprocessing

pdtestdata = pd.read_csv('recorded_data.csv', delimiter=',')
pdtestdata = pdtestdata.drop(pdtestdata.columns[0], axis=1) # Remove ID
print(pdtestdata)

toAvg = 0
avgBy = 5
toReshape = 1
reshapeBy = 10

if (toAvg):
    pdtestdata = ((pdtestdata + pdtestdata.shift(-1) + pdtestdata.shift(-2) + pdtestdata.shift(-3) + pdtestdata.shift(-4)) / 5)[::5]

if (toReshape):
    pdtestdata = pd.DataFrame(np.reshape(pdtestdata.values,(600,120)),  columns=list(range(120)))


pdtestdata = pdtestdata.reset_index(drop=True)
print(pdtestdata)

pdtestdata.to_csv('processed_data.csv', sep=',')