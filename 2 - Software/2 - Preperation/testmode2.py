# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 13:34:33 2017

@author: diary
"""

from scipy.stats import mode

listed = [1,2,3,4,1,2,3,4,4,4,4,4,4]
print(mode(listed)[0][0])
print(mode(listed)[1][0])