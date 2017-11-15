# -*- coding: utf-8 -*-
"""
@author: Jun Hao
"""
print('learning')
#Set print command to print to file
#import sys
#sys.stdout = open("Output.txt", "w")

#Print current time on computer
from datetime import datetime
print (str(datetime.now()))

#Implement simple timer
import time
tfulls = time.time()

# Config.ini
reshapeBy = 40 # Set number of inputs per sample for Machine Learning

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

#Sort data into columns -> For some reason can't extract class column using the better(next) method
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

#Sort data into a whole array and extract necessary data
testdata = np.genfromtxt ('processed_data.csv', delimiter=",")
testdata = np.delete(testdata, (0), axis=0)
X = testdata[:, 1:(reshapeBy*12)+1]



#Data pre-processing
from sklearn import preprocessing

##Encode output variable
le = preprocessing.LabelEncoder()
le.fit(['Standing', 'WaveHands', 'BusDriver', 'FrontBack', 'SideStep', 'Jumping'])
#print(list(le.classes_))
y = []
y = le.transform(column[str(reshapeBy*12)])

#Normalize data
normalized_X = preprocessing.normalize(X)


#Evaluate model
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import KFold
#from sklearn.metrics import confusion_matrix

n_splits_val = 10
kfold = KFold(n_splits=n_splits_val, shuffle=True)

#KNN
print(' ')
print('Nearest Neighbors')
print(' ')
#tknns = time.time()
fold_index = 0
#avg_accuracy_knn = 0
for train, test in kfold.split(normalized_X, y=None, groups=None):
    tparts = time.time()
    knn_model = KNeighborsClassifier(n_neighbors=5, weights='uniform', algorithm='auto', leaf_size=30, p=2, metric='minkowski', metric_params=None, n_jobs=-1).fit(normalized_X[train], y[train])
    knn_predictions = knn_model.predict(normalized_X[test])
    #accuracy = knn_model.score(normalized_X[test], y[test])
    #cm = confusion_matrix(y[test], knn_predictions)
    #tparte = time.time()
    #avg_accuracy_knn += accuracy
    #print('In the %i fold, the classification accuracy is %f' %(fold_index, accuracy))
    #print('And the confusion matrix is: ')
    #print(cm)
    #print('This fold took %f seconds' %(tparte-tparts))
    fold_index +=1
    #print(' ')
#avg_accuracy_knn /= n_splits_val
#tknne = time.time()

#RF
print(' ')
print('Random Forest')
print(' ')
#trfs = time.time()
fold_index = 0
#avg_accuracy_rf = 0
for train, test in kfold.split(normalized_X, y=None, groups=None):
    tparts = time.time()
    rf_model = RandomForestClassifier(n_jobs=-1).fit(normalized_X[train], y[train])
#    rf_predictions = rf_model.predict(normalized_X[test])
#    accuracy = rf_model.score(normalized_X[test], y[test])
#    cm = confusion_matrix(y[test], rf_predictions)
#    tparte = time.time()
#    avg_accuracy_rf += accuracy
#    print('In the %i fold, the classification accuracy is %f' %(fold_index, accuracy))
#    print('And the confusion matrix is: ')
#    print(cm)
#    print('This fold took %f seconds' %(tparte-tparts))
    fold_index +=1
#    print(' ')
#avg_accuracy_rf /= n_splits_val
#trfe = time.time()
#print(' ')

#Results
#print('Results:')
#print(' ')
#print('Nearest Neighbors took %f seconds' %(tknne-tknns))
#print('with an average accuracy of %f%%' %(avg_accuracy_knn*100))
#print(' ')
#print('Random Forest took %f seconds' %(trfe-trfs))
#print('with an average accuracy of %f%%' %(avg_accuracy_rf*100))
#print(' ')
#print(' ')


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
joblib.dump(knn_model, 'model_knn.pkl', protocol=2) #Save Model
#knn_model = joblib.load('model_knn.pkl') #Load Model
joblib.dump(rf_model, 'model_rf.pkl', protocol=2) #Save Model
#rf_model = joblib.load('model_rf.pkl') #Load Model

#
tfulle = time.time()
print('The whole code took %f seconds' %(tfulle-tfulls))
