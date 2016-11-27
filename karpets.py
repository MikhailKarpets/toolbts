# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 14:31:42 2016

@author: device
"""

import pandas as pd
import numpy as np

data = pd.read_csv('F:\mike\hse\exactpro\JBoss.csv')

data_to_print = data['Description'][:5];

print(data_to_print)