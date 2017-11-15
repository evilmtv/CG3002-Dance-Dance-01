# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 16:13:54 2017

@author: diary
"""

from scipy import stats
list = ['Jumping', 'Jumping', 'loling', 'Jumping', 'asd']
print(stats.mode(list)[0][0])