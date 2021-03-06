# -*- coding: utf-8 -*-
"""
@author: Jun Hao
"""

#Print current time on computer
from datetime import datetime
print (str(datetime.now()))

#Implement simple timer
import time
tfulls = time.time()

# Config.ini
reshapeBy = 50 # Set number of inputs per sample for Machine Learning
#sys.stdout = open("OutputComb.txt", "w") # Set print command to print to file

# Initialize random seed
#import random
#from random import randint
#random.seed(a=None, version=2)
#randomStanding = randint(0, 599)
#randomWaveHands = randint(600, 1199)
#randomBusDriver = randint(1199, 1799)
#randomFrontBack = randint(1799, 2399)
#randomSideStep = randint(2399, 2999)
#randomJumping = randint(2999, 3599)

# Sort data into columns -> For some reason can't extract class column using the better(next) method
import csv
import numpy as np
with open('processed_data.csv') as csvfile:
    reader=csv.reader(csvfile,delimiter=',')
    headers = next(reader)
    column = {}
    for h in headers:
        column[h] = []
    for row in reader:
        for h, v in zip(headers, row):
            column[h].append(v)

# Sort data into a whole array and extract necessary data
testdata = np.genfromtxt ('processed_data.csv', delimiter=",")
print(testdata.shape)
testdata = np.delete(testdata, (0), axis=0)
testdata = np.delete(testdata, (451), axis=1)
testdata = np.delete(testdata, (0), axis=1)
print(testdata.shape)
X = testdata[:, 0:(reshapeBy*9)+1]
print(X.shape)



# Data pre-processing
from sklearn import preprocessing

# Encode output variable
le = preprocessing.LabelEncoder()
le.fit(['standing', 'wavehands', 'busdriver', 'frontback', 'sidestep', 'jumping', 'jumpingjack', 'turnclap', 'squatturnclap', 'windowcleaning', 'windowcleaner360', 'logout'])
#print(list(le.classes_))
y = []
y = le.transform(column['451'])
#y = column['481']

#Normalize data
normalized_X = preprocessing.normalize(X)
print(normalized_X.shape)


# Evaluate model
print('Learning')
#from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import KFold
from sklearn.metrics import confusion_matrix

n_splits_val = 10
kfold = KFold(n_splits=n_splits_val, shuffle=True)

# KNN
#print(' ')
#print('Nearest Neighbors')
#print(' ')
#tknns = time.time()
#fold_index = 0
#avg_accuracy_knn = 0
#for train, test in kfold.split(normalized_X, y=None, groups=None):
#    tparts = time.time()
#    knn_model = KNeighborsClassifier(n_neighbors=5, weights='uniform', algorithm='auto', leaf_size=30, p=2, metric='minkowski', metric_params=None, n_jobs=-1).fit(normalized_X[train], y[train])
#    knn_predictions = knn_model.predict(normalized_X[test])
#    accuracy = knn_model.score(normalized_X[test], y[test])
#    cm = confusion_matrix(y[test], knn_predictions)
#    tparte = time.time()
#    avg_accuracy_knn += accuracy
#    print('In the %i fold, the classification accuracy is %f' %(fold_index, accuracy))
#    print('And the confusion matrix is: ')
#    print(cm)
#    print('This fold took %f seconds' %(tparte-tparts))
#    fold_index +=1
#    print(' ')
#avg_accuracy_knn /= n_splits_val
#tknne = time.time()

# Random Forests
print(' ')
print('Random Forests')
print(' ')
trfs = time.time()
fold_index = 0
avg_accuracy_rf = 0
for train, test in kfold.split(normalized_X, y=None, groups=None):
    tparts = time.time()
    rf_model = RandomForestClassifier(n_jobs=-1).fit(normalized_X[train], y[train])
    print(normalized_X[train].shape)
    rf_predictions = rf_model.predict(normalized_X[test])
    accuracy = rf_model.score(normalized_X[test], y[test])
    cm = confusion_matrix(y[test], rf_predictions)
    tparte = time.time()
    avg_accuracy_rf += accuracy
    print('In the %i fold, the classification accuracy is %f' %(fold_index, accuracy))
    print('And the confusion matrix is: ')
    print(cm)
    print('This fold took %f seconds' %(tparte-tparts))
    fold_index +=1
    print(' ')
avg_accuracy_rf /= n_splits_val
trfe = time.time()
print(' ')

# Results
print('Results:')
print(' ')
#print('Nearest Neighbors took %f seconds' %(tknne-tknns))
#print('with an average accuracy of %f%%' %(avg_accuracy_knn*100))
#print(' ')
print('Random Forest took %f seconds' %(trfe-trfs))
print('with an average accuracy of %f%%' %(avg_accuracy_rf*100))
print(' ')
print(' ')


#Extract some random values
#sample = normalized_X[[randomStanding,randomWaveHands,randomBusDriver,randomFrontBack,randomSideStep,randomJumping],:]
#sampletruth = y[[randomStanding,randomWaveHands,randomBusDriver,randomFrontBack,randomSideStep,randomJumping],]

#print('Test Sample')
#print('Sample data(normalized):')
#print(sample)
#print(' ')
#print('Correct result:')
#print(sampletruth)
#print('KNN predicted result:')
#print(knn_model.predict(sample))
#print('RF predicted result:')
#print(rf_model.predict(sample))


#Save models for deployment use
from sklearn.externals import joblib
#joblib.dump(knn_model, 'model_knn.pkl', protocol=2) #Save Model
#knn_model = joblib.load('model_knn.pkl') #Load Model
joblib.dump(rf_model, 'model_rf.pkl', protocol=2) #Save Model
#rf_model = joblib.load('model_rf.pkl') #Load Model

#
tfulle = time.time()
print('The whole code took %f seconds' %(tfulle-tfulls))
