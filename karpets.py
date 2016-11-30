# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 14:31:42 2016

@author: device
"""

import pandas as pd
import re
#import numpy as np
number_of_bug_descr = list()
all_projects_list = list()
for i in range(2,3):
    str_path = "F:\\mike\\hse\\exactpro\\all_projects\\JBoss%d.csv" % i
    data = pd.read_csv(str_path)
    data_description0 = data['Description'][1:]
    data_description0.dropna(inplace = True)
    data_description0.to_frame()
    data_len = len(data_description0)
    number_of_bug_descr.append(data_len)
    zeros_df = pd.DataFrame(0, index=data_description0.index, columns=['HasStackTrace'])
    data_description = pd.concat([data_description0, zeros_df], axis=1)
    
    subset = data_description[['Description', 'HasStackTrace']]
    list_data_descr_and_stack_trace_flag = [list(x) for x in subset.values]
    
    #LAST VARIANT (29/11/2016 15.00)
    pattern = re.compile('(?:(((\\n.*ERROR.*)+)?((.*ERROR.*\\n)+)?((.*[a-zA-Z]Exception.*\\n)+)?((.*[a-zA-Z]Error.*\\n)+)?((.*at .*[(].*(?:java|(?:Unknown Source|Native Method)).*[)].*)+))|((((?:((\\n.*ERROR.*)+)|((.*ERROR.*\\n)+)))+)((((.*[a-zA-Z]Exception.*\\n)+)))))')
    
    if i == 2:
        del list_data_descr_and_stack_trace_flag[58]
        del list_data_descr_and_stack_trace_flag[810]
    
    for k,item in enumerate(list_data_descr_and_stack_trace_flag):
#        print(k)
        text = item[0]
    #    print(text)
        if pattern.search(text):
            list_data_descr_and_stack_trace_flag[k][1] = 1
            temp_str = pattern.sub('', text)
            temp_str = " ".join(temp_str.split())
            list_data_descr_and_stack_trace_flag[k][0] = temp_str
    all_projects_list = all_projects_list + list_data_descr_and_stack_trace_flag
#    print(list_data_descr_and_stack_trace_flag)
#print(all_projects_list)
print('Number of all descriptions: ')
print(len(all_projects_list))
print('Number of descriptions from projects 1,2,3: ')
print(number_of_bug_descr)
for j in range(80,100):
    print('|||||||||||||||||||||BEGIN||||||||||||||||||||')
    print(j)
    print('|||||||||||||||||||||BEGIN||||||||||||||||||||||||||||||')
    print(all_projects_list[j][0])
    