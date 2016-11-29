# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 14:31:42 2016

@author: device
"""

import pandas as pd
import re
import numpy as np


data = pd.read_csv('F:\mike\hse\exactpro\JBoss.csv')
data_description0 = data['Description'][1:]
data_description0.dropna(inplace = True)
data_description0.to_frame()
data_len = len(data_description0)
zeros_df = pd.DataFrame(0, index=data_description0.index, columns=['HasStackTrace'])
data_description = pd.concat([data_description0, zeros_df], axis=1)

#data_description = data_description.as_matrix()
subset = data_description[['Description', 'HasStackTrace']]
list_data_descr_and_stack_trace_flag = [list(x) for x in subset.values]



#pattern = re.compile('at .*java.*\\n+')
#pattern = re.compile('\\n.*ERROR.*')
#pattern = re.compile('(.*ERROR.*\\n)+.*[a-zA-Z]Exception.*')
#pattern = re.compile('(.*ERROR.*\\n)+?.*[a-zA-Z]Exception.*')
#ok below (106)
#pattern = re.compile('(.*ERROR.*\\n)+?(.*[a-zA-Z]Exception.*)+?')
#pattern = re.compile('(^ERROR.*\\n)?(.*ERROR.*\\n)+?(.*[a-zA-Z]Exception.*\\n)+?')
#OK below (103&106)
#pattern = re.compile('((\\n.*ERROR.*)+)?((.*ERROR.*\\n)+)?((.*[a-zA-Z]Exception.*\\n)+)?((.*[a-zA-Z]Error.*\\n)+)?')
#OK below (103&106)
#pattern = re.compile('((\\n.*ERROR.*)+)?((.*ERROR.*\\n)+)?((.*[a-zA-Z]Exception.*\\n)+)?((.*[a-zA-Z]Error.*\\n)+)?((.*at .*java.*\\n)+)')
#OK below
#pattern = re.compile('((\\n.*ERROR.*)+)?((.*ERROR.*\\n)+)?((.*[a-zA-Z]Exception.*\\n)+)?((.*[a-zA-Z]Error.*\\n)+)?((.*at .*[(].*java.*[)].*\\n)+)')
#OK
#pattern = re.compile('((\\n.*ERROR.*)+)?((.*ERROR.*\\n)+)?((.*[a-zA-Z]Exception.*\\n)+)?((.*[a-zA-Z]Error.*\\n)+)?((.*at .*[(].*java.*[)].*)+)')
#OK
#pattern = re.compile('((\\n.*ERROR.*)+)?((.*ERROR.*\\n)+)?((.*[a-zA-Z]Exception.*\\n)+)?((.*[a-zA-Z]Error.*\\n)+)?((.*at .*[(].*(?:java|(?:Unknown Source|Native Method)).*[)].*)+)')
#OK except 249
#pattern = re.compile('((\\n.*ERROR.*)+)?((.*ERROR.*\\n)+)?((.*[a-zA-Z]Exception.*\\n)+)?((.*[a-zA-Z]Error.*\\n)+)?((.*at .*[(].*(?:java|(?:Unknown Source|Native Method)).*[)].*)+)')

#LAST VARIANT (29/11/2016 15.00)
pattern = re.compile('(?:(((\\n.*ERROR.*)+)?((.*ERROR.*\\n)+)?((.*[a-zA-Z]Exception.*\\n)+)?((.*[a-zA-Z]Error.*\\n)+)?((.*at .*[(].*(?:java|(?:Unknown Source|Native Method)).*[)].*)+))|((((?:((\\n.*ERROR.*)+)|((.*ERROR.*\\n)+)))+)((((.*[a-zA-Z]Exception.*\\n)+)))))')


#(((.*[a-zA-Z]Exception.*\\n)+)?)
#pattern = re.compile('((\\n.*ERROR.*)+?(\\n.*[a-zA-Z0-9]Exception.*)?)?\\n.*at .*([^\\n\s]*[.][^\\n\s]*)+(java)?.*[(].*[)]')
#ok below (except 3,106 etc)
#pattern = re.compile('((\\n.*ERROR.*)+?(\\n.*[a-zA-Z0-9]Exception.*)?)?(\\n.*at .*([^\\n\s]*[.][^\\n\s]*)+(java)?.*[(].*[)](\\nCaused by:.*)?(\\n([^\\n\s]*[.][^\\n\s]*)+.*[(].*java.*[)])?)+')
#pattern = re.compile('((((^|\\n).*ERROR.*)+)?(\\n.*[a-zA-Z0-9]Exception.*)?)?(\\n.*at .*([^\\n\s]*[.][^\\n\s]*)+(java)?.*[(].*[)](\\nCaused by:.*)?(\\n([^\\n\s]*[.][^\\n\s]*)+.*[(].*java.*[)])?)+')
#pattern = re.compile('((((^|\\n).*ERROR.*)+)?(\\n.*[a-zA-Z]Exception.*)?)?(\\n.*at .*([^\\n\s]*[.][^\\n\s]*)+.*[(].*java.*[)](\\nCaused by:.*)?(\\n([^\\n\s]*[.][^\\n\s]*)+.*[(].*java.*[)])?)+')

for i,item in enumerate(list_data_descr_and_stack_trace_flag):
    text = item[0]
    print(text)
    if pattern.search(text):
        list_data_descr_and_stack_trace_flag[i][1] = 1
        temp_str = pattern.sub('', text)
        temp_str = " ".join(temp_str.split())
        list_data_descr_and_stack_trace_flag[i][0] = temp_str
print(list_data_descr_and_stack_trace_flag)
    



#for index,row in data_description.iterrows():
##    print(row['Description'])
#    text = data_description.iloc[index]['Description']
##    print(text)
#    if isinstance(text, str):
#        if pattern.search(text):
##            print('----------------------------BEGIN-------------------------')
##            print('-------------------------'+str(index)+'----------------------------')
##            print(row)
##            print('|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')
#            temp_str = pattern.sub('', text)
#            temp_str = " ".join(temp_str.split())
#            data_description['Description'][index] = temp_str
##            print(data_description[index])
##            matches = pattern.findall(row)
##            print(matches)
##            print('-------------------------'+str(index)+'----------------------------')
##            print('-------------------------END----------------------------')
##            print()
##            print()
#    else:
#        print(type(row))
#        print(row)
#for x in data_description:
#    print(x)