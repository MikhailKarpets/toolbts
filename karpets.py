# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 14:31:42 2016

@author: device
"""

import pandas as pd
import re
#import numpy as np


def check_pattern(pattern0, text, num_pattern):
    if pattern0.search(text):
        temp_str = 'PATTERN %d' % num_pattern  
        print(temp_str) 
    #   list_data_descr_and_stack_trace_flag[k][1] = 1
        temp_str = pattern0.sub('', text)
    #   temp_str = " ".join(temp_str.split())
        print('|||||||||||||||||||||||||||||||BEGIN MATCHES|||||||||||||||||||||||||||')
        matches = pattern0.findall(text)
        print(matches)
        print('|||||||||||||||||||||||||||||||END MATCHES|||||||||||||||||||||||||||||')
        print()
        print()
        print('|||||||||||||||||||||||||||||||BEGIN clean TEXT|||||||||||||||||||||||||||')
        print(temp_str)
        print('|||||||||||||||||||||||||||||||END clean TEXT|||||||||||||||||||||||||||')
        print()
        print()    
        return temp_str
    else:
        return text


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
    
    #LAST VARIANT (01/12/2016 00.00)
    pattern0 = re.compile('(?:(((\\n.*ERROR.*)+)?((.*ERROR.*\\n)+)?((.*[a-zA-Z]Exception.*\\n)+)?((.*[a-zA-Z]Error.*\\n)+)?((.*at .*[(].*(?:java|(?:Unknown Source|Native Method)).*[)].*)+))|((((?:((\\n.*ERROR.*)+)|((.*ERROR.*\\n)+)))+)((((.*[a-zA-Z]Exception.*\\n)+)))))')
    pattern1 = re.compile('(  ?:.*ERROR.*|(?:.*INFO.*|(?:.*WARN.*|(?:.*CLOSE_WAIT.*|(?:.*BLOCKED.*|(?:.*DEBUG.*|.*WAITING.*))))))') 
#    сомнения в работоспособности (ниже)
#    pattern2 = re.compile('(?:((.*[0-9][0-9]:[0-9][0-9]:[0-9][0-9].*[[]error[]].*client.*)+)|(?:((.*at line.*\\n.*at line.*\\n.*at line.*\\n)+)|(?:((.*java.*[(].*[)].*\\n.*java.*[(].*[)].*\\n.*java.*[(].*[)].*\\n.*java.*[(].*[)].*\\n)+)|(?:((.*[Cc]aused by.*java.*\\n.*[Cc]aused by.*java.*\\n)+)|( ( [a-zA-Z]+\.[a-zA-Z]+\.[a-zA-Z]+[(](?:.*java.*|(?:.*Native Method.*|.*No such file or directory.*))[)])+)))))')
    
#    ok
    pattern2 = re.compile('([a-zA-Z]+\.[a-zA-Z]+\.[a-zA-Z]+[(](?:.*java.*|(?:.*Native Method.*|.*No such file or directory.*))[)])')
#    ok
    pattern3 = re.compile('.*[Cc]aused by.*java.*\\n(.*[Cc]aused by.*java.*\\n)+')
#    ok    
    pattern4 = re.compile('.*at line.*\\n.*at line.*\\n((.*at line.*\\n)+)')
#    ok
    pattern5 = re.compile('((.*[0-9][0-9]:[0-9][0-9]:[0-9][0-9].*[[]error[]].*client.*)+)')
#    ok
    pattern6 = re.compile('.*java.*[(].*[)].*\\n(.*java.*[(].*[)].*\\n)+')
    pattern7 = re.compile('.*ERROR.*\\n')
    pattern8 = re.compile('.*[(].*".*".*=>.*".*".*[)].*')
    pattern9 = re.compile('failure description:.*[{].*[}]', re.DOTALL)
    pattern10 = re.compile('.*WFLYPRT.*')
    
    arr_patterns = [pattern0, pattern1, pattern2, pattern3, pattern4, pattern5, pattern6, pattern7, pattern8, pattern9]
   
    if i == 2:
        del list_data_descr_and_stack_trace_flag[58]
        del list_data_descr_and_stack_trace_flag[810]
    
    for k,item in enumerate(list_data_descr_and_stack_trace_flag):
        if k < 16:
            continue
        if k == 25:
            print('|||||||||||||||||||||||||||||||||||||||||||')
            print('|||||||||||||||||||||||||||||||||||||||||||')
            print('|||||||||||||||||||||||||||||||||||||||||||')
            print('|||||||||||||||||||||||||||||||||||||||||||')
            print('|||||||||||||||||||||||||||||||||||||||||||')
            print('|||||||||||||||||||||||||||||||||||||||||||')
            print('|||||||||||||||||||||||||||||||||||||||||||')
            print('|||||||||||||||||||||||||||||||||||||||||||')
            print('|||||||||||||||||||||||||||||||||||||||||||')
            print('|||||||||||||||||||||||||||||||||||||||||||')
            break
        print('|||||||||||NUMBER OF TEXT||||||||||||')
        print(k)
        text = item[0]
        print('|||||||||||||||||||||||||||||||BEGIN TEXT with trash|||||||||||||||||||||||||||')
        print(text)
        print('|||||||||||||||||||||||||||||||END TEXT with trash|||||||||||||||||||||||||||')
        print()
        print()
        for i, pattern in enumerate(arr_patterns):
            text = check_pattern(pattern, text, i)
            
                

            
#            list_data_descr_and_stack_trace_flag[k][0] = temp_str
#    all_projects_list = all_projects_list + list_data_descr_and_stack_trace_flag
#    print(list_data_descr_and_stack_trace_flag)
#print(all_projects_list)
#print('Number of all descriptions: ')
#print(len(all_projects_list))
#print('Number of descriptions from projects 1,2,3: ')
#print(number_of_bug_descr)
#for j in range(80,100):
#    print('|||||||||||||||||||||BEGIN||||||||||||||||||||')
#    print(j)
#    print('|||||||||||||||||||||BEGIN||||||||||||||||||||||||||||||')
#    print(all_projects_list[j][0])
    