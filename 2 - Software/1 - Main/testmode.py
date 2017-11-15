# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 16:13:54 2017

@author: diary
"""
import numpy as np
from scipy import stats
list2 = ['Jumping', 'Jumping', 'loling', 'Jumping', 'asd']
X = np.array(['Jumping', 'Jumping', 'loling', 'Jumping', 'asd'])

 
print(stats.mode(list2)[0][0])
print(range(1, 4))