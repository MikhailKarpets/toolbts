# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 14:31:42 2016

@author: device
"""

import pandas as pd
import numpy as np

data = pd.read_csv('F:\mike\hse\exactpro\JBoss.csv')

#data_to_print = data['Description'][:5];
#print(data_to_print)

data_to_write = data['Description'][:3]

f = open("F:\mygit\descr.txt","r")
o = open("F:\\mygit\\text.txt",'w', newline="\r\n")
for line in f:
    print(line)
    o.write(line)
o.close()
f.close()

