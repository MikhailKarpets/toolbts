# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 14:31:42 2016

@author: device
"""

import pandas as pd
import re
#import numpy as np

data = pd.read_csv('F:\mike\hse\exactpro\JBoss.csv')
data_description = data['Description'][250:252]

#pattern = re.compile('at .*java.*\\n+')
#pattern = re.compile('\\n.*ERROR.*')
#pattern = re.compile('((\\n.*ERROR.*)+?(\\n.*[a-zA-Z0-9]Exception.*)?)?\\n.*at .*([^\\n\s]*[.][^\\n\s]*)+(java)?.*[(].*[)]')
#pattern = re.compile('((\\n.*ERROR.*)+?(\\n.*[a-zA-Z0-9]Exception.*)?)?(\\n.*at .*([^\\n\s]*[.][^\\n\s]*)+(java)?.*[(].*[)](\\nCaused by:.*)?(\\n([^\\n\s]*[.][^\\n\s]*)+.*[(].*java.*[)])?)+')
#pattern = re.compile('((((^|\\n).*ERROR.*)+)?(\\n.*[a-zA-Z0-9]Exception.*)?)?(\\n.*at .*([^\\n\s]*[.][^\\n\s]*)+(java)?.*[(].*[)](\\nCaused by:.*)?(\\n([^\\n\s]*[.][^\\n\s]*)+.*[(].*java.*[)])?)+')
pattern = re.compile('((((^|\\n).*ERROR.*)+)?(\\n.*[a-zA-Z]Exception.*)?)?(\\n.*at .*([^\\n\s]*[.][^\\n\s]*)+.*[(].*java.*[)](\\nCaused by:.*)?(\\n([^\\n\s]*[.][^\\n\s]*)+.*[(].*java.*[)])?)+')


for index,row in data_description.iteritems():
    if isinstance(row, str):
        if pattern.search(row):
            print('----------------------------BEGIN-------------------------')
            print('-------------------------'+str(index)+'----------------------------')
            print(row)
            print('-------------------------------------------------------------------')
            temp_str = pattern.sub('', row)
#            temp_str = " ".join(temp_str.split())
            data_description[index] = temp_str
            print(data_description[index])
            print('-------------------------'+str(index)+'----------------------------')
            print('-------------------------END----------------------------')
            print()
            print()
    

#^.+Exception[^\n]++(\s+at .++)+

#pattern = re.compile('at .*java.*\\n+')

#pattern = re.compile('at .*[)].*\\n+')
#pattern = re.compile('ERROR')
#pattern = re.compile('javax.faces.FacesException: java.lang.ClassNotFoundException: No ClassLoaders found for: com.google.code.kaptcha.servlet.CaptchaServlet')
#pattern = re.compile('\n[^\n]*ERROR')
#pattern = re.compile('[^\\n]*ERROR([^\\n]*\\n){2,3}(.*at.*\\n)+')
#pattern = re.compile('\\n[^\\n]*ERROR([^\\n]*\\n){2,3}(.*at.*\\n)+')
#pattern = re.compile('(\\n[^\\n]*ERROR)+( [^\\n]*(\\s)+at )+[^\\n]*(\\s)')

#count = 0
#for item in data_description:
#    re.sub('at .*java.*\\n+', '', item)
#    count = count + 1
#    print("-----------------------------------ITEM IS")
#    #print(item)
#    print("-----------------------------------RESULT IS")
#    result = pattern.finditer(item)
#    print(count)
#    for match in result:
#        print("---")
#        temp = match.group()
#        print(temp)
    
    #print(result)
    #print("-----------------------------------RESULT GROUP IS")
    #print result.group()

#for i,line in enumerate(data_description):
#    print(line)