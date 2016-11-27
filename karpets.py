# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 14:31:42 2016

@author: device
"""

import pandas as pd
import re
#import numpy as np

data = pd.read_csv('F:\mike\hse\exactpro\JBoss.csv')
data_description = data['Description'][1:100]
#print(data_description[104])

#i = 0;
#for x in data_description:
#    i = i+1;
#    if i >=102:
#        print(x)

#^.+Exception[^\n]++(\s+at .++)+


pattern = re.compile('at .*java.*\\n+')
#pattern = re.compile('at .*[)].*\\n+')
#pattern = re.compile('ERROR')
#pattern = re.compile('javax.faces.FacesException: java.lang.ClassNotFoundException: No ClassLoaders found for: com.google.code.kaptcha.servlet.CaptchaServlet')
#pattern = re.compile('\n[^\n]*ERROR')
#pattern = re.compile('[^\\n]*ERROR([^\\n]*\\n){2,3}(.*at.*\\n)+')
#pattern = re.compile('\\n[^\\n]*ERROR([^\\n]*\\n){2,3}(.*at.*\\n)+')
#pattern = re.compile('(\\n[^\\n]*ERROR)+( [^\\n]*(\\s)+at )+[^\\n]*(\\s)')

count = 0
for item in data_description:
    count = count + 1
    print("-----------------------------------ITEM IS")
    #print(item)
    print("-----------------------------------RESULT IS")
    result = pattern.finditer(item)
    print(count)
    for match in result:
        print("---")
        temp = match.group()
        print(temp)
    
    #print(result)
    #print("-----------------------------------RESULT GROUP IS")
    #print result.group()


#    
#f = open("F:\mygit\descr.txt","r")
#
#for line in f:
#    o = open("F:\\mygit\\text.txt",'w', newline="\r\n")
#    o.write(str(line))
#    o.close()
#
#f.close()

