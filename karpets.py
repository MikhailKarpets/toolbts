from nltk.corpus import stopwords 
import nltk
from nltk.util import ngrams 
import csv 
import string 

import pandas as pd
import re
#import numpy as np


def filter_pattern(arr_pattern, text):
#    print('||||||||||||||||||||RAW TEXT|||||||||||||||||||||||')
#    print(text)
#    print('||||||||||||||||||||RAW TEXT|||||||||||||||||||||||')
#    print()
    stack_trace_flag = 0
    temp_str = ' '
#    cleaned_text = ' '
#    cleaned_text = text
    temp_str = text
    for i, pattern in enumerate(arr_pattern):
#        print('.')
        if pattern.search(temp_str):
#            pattern_declaration = 'PATTERN %d' % i  
#            print(pattern_declaration)
            if ((i < 12) or (i == 17) or (i == 26)): #change i if number of stack-trace regex changes! 
                stack_trace_flag = 1
#            matches = pattern.findall(temp_str)
            temp_str = pattern.sub('', temp_str)
#            cleaned_text = temp_str
#            temp_str = " ".join(temp_str.split())
#            print('|||||||||||||||||||||||||||||||BEGIN MATCHES||||||||||||||||||||||||||||||') #mt
#            print(matches) #mt
#            print('|||||||||||||||||||||||||||||||END MATCHES||||||||||||||||||||||||||||||||') #mt
#            print() #mt
#            print() #mt 
#            print('|||||||||||||||||||||||||||||||BEGIN cleaned TEXT|||||||||||||||||||||||||||')
#            print(cleaned_text)
#            print('|||||||||||||||||||||||||||||||END cleaned TEXT|||||||||||||||||||||||||||||')
#            print()
#            print()    
#    print()
#    print()
#    print('|||||||||||||||||||||||||||||||BEGIN cleaned TEXT|||||||||||||||||||||||||||') #ct
#    cleaned_text = " ".join(cleaned_text.split()) #for text 9 ONLY!!!
#    print(cleaned_text) #ct
#    print('|||||||||||||||||||||||||||||||END cleaned TEXT|||||||||||||||||||||||||||||') #ct
#    print() #ct
#    print() #ct
    temp_str = " ".join(temp_str.split())
    return [temp_str, stack_trace_flag]

pattern0 = re.compile('(?:(.*WFLY.*)|(?:.*ERROR.*|(?:.*INFO.*|(?:.*WARN.*|(?:.*CLOSE_WAIT.*|(?:.*BLOCKED.*|(?:.*DEBUG.*|.*WAITING.*)))))))') 
pattern1 = re.compile('(?:(((\\n.*ERROR.*)+)?((.*ERROR.*\\n)+)?((.*[a-zA-Z]Exception.*\\n)+)?((.*[a-zA-Z]Error.*\\n)+)?((.*at .*[(].*(?:java|(?:Unknown Source|Native Method)).*[)].*)+))|((((?:((\\n.*ERROR.*)+)|((.*ERROR.*\\n)+)))+)((((.*[a-zA-Z]Exception.*\\n)+)))))')
pattern2 = re.compile('.*(?:waiting|locked).*0x.*[(].*[)].*')
pattern3 = re.compile('.*0x.*0x.*')
pattern4 = re.compile('.*(?:(".*ActiveMQ.*")|(".*Thread-7.*")).*')
pattern5 = re.compile('([a-zA-Z]+\.[a-zA-Z]+\.[a-zA-Z]+[(](?:.*java.*|(?:.*Native Method.*|.*No such file or directory.*))[)])')
pattern6 = re.compile('.*[Cc]aused by.*java.*\\n(.*[Cc]aused by.*java.*\\n)+') 
pattern7 = re.compile('.*at line.*\\n.*at line.*\\n((.*at line.*\\n)+)')
pattern8 = re.compile('((.*[0-9][0-9]:[0-9][0-9]:[0-9][0-9].*[[]error[]].*client.*)+)')
pattern9 = re.compile('.*java.*[(].*[)].*\\n.*java.*[(].*[)].*\\n')
#    pattern7 = re.compile('.*ERROR.*\\n')
pattern10 = re.compile('.*[(].*".*".*=>.*".*".*[)].*')
pattern11 = re.compile('failure description:.*[{].*[}]', re.DOTALL)
#    pattern11 = re.compile('.*WFLYPRT.*')
#ok
#pattern12 = re.compile('[\\s][{][\\s].*[\\s][}][\\s]', re.DOTALL)
pattern12 = re.compile('\\n[{]\\r\\n.*\\r\\n[}]\\r', re.DOTALL)
pattern13 = re.compile('[/][^\\s]*=[^\\s]*[/][^\\s]*=[^\\s]*')
pattern14 = re.compile('[^\\s]+[.][^\\s"]+')
pattern15 = re.compile('{{.*}}') 
pattern16 = re.compile('[^\\s]+[/][^\\s]+')
pattern17 = re.compile('.*Event.*receive.*from remote server.*\\nInternal Server Error.*')
pattern18 = re.compile('<.*>\\s.*<[/].*>\\s', re.DOTALL)
pattern19 = re.compile('\\s.*=.*\\s')
pattern20 = re.compile('(?:({panel})|(?:({code[^\\s]*})|(?:({noformat})|({quote}))))')
pattern21 = re.compile('[a-z]+[A-Z][a-z]+( )?[{].*[}]', re.DOTALL)
pattern22 = re.compile('[A-Z][a-z]+[A-Z][a-z]+[(].*[)]')
pattern23 = re.compile('{.*return.*}', re.DOTALL)
pattern24 = re.compile('[^\\s]*@[^\\s]*')
pattern25 = re.compile('[a-z]+[A-Z][a-z]+[^\\s]*')
pattern26 = re.compile('[0-9]+.*has been deprecated')
pattern27 = re.compile('[[][0-9][0-9]:[0-9][0-9] (?:(PM)|(AM))[]].*:')
pattern28 = re.compile('@[^\\s]*')
pattern29 = re.compile('[.][a-z]*[^\\s]*')
pattern30 = re.compile('<[^\\s]*>')
pattern31 = re.compile('<[[].*[]]>')
pattern32 = re.compile('[[]disconnected.*[/][]]')
pattern33 = re.compile('[-][-][a-z]*')
pattern34 = re.compile('try.*{.*}')
pattern35 = re.compile('catch.*{.*}')
pattern36 = re.compile('{.*throw.*}')
pattern37 = re.compile('check.*{.*}')
pattern38 = re.compile('public void')
pattern39 = re.compile('private void')
pattern40 = re.compile('[[][[].*[]][]]')
pattern41 = re.compile('<.*[/]>')

###############################################################
###############################################################
pattern42 = re.compile('(?:a2p|ac|addgroup|adduser|agrep|alias|apropos|apt-cache|apt-get|aptitude|ar|arch|arp|as|aspell|at|awk|basename|bash|bc|bdiff|bfs|bg|biff|break|bs|bye|cal|calendar|cancel|cat|cc|cd|cfdisk|chdir|checkeq|checknr|chfn|chgrp|chkey|chmod|chown|chroot|chsh|cksum|clear|cmp|col|comm|compress|continue|cp|cpio|crontab|csh|csplit|ctags|cu|curl|cut|date|dc|dd|delgroup|deluser|depmod|deroff|df|dhclient|diff|dig|dircmp|dirname|dmesg|dos2unix|dpkg|dpost|du|echo|ed|edit|egrep|eject|elm|emacs|enable|env|eqn|ex|exit|expand|expr|fc|fdisk|fg|fgrep|file|find|findsmb|finger|fmt|fold|for|foreach|free|fsck|ftp|fuser|gawk|getfacl|gpasswd|gprof|grep|groupadd|groupdel|groupmod|gunzip|gview|gvim|gzip|halt|hash|hashstat|head|help|history|host|hostid|hostname|id|ifconfig|ifdown|ifquery|ifup|info|init|insmod|iostat|ip|isalist|iwconfig|jobs|join|keylogin|kill|killall|ksh|last|ld|ldd|less|lex|link|ln|lo|locate|login|logname|logout|losetup|lp|lpadmin|lpc|lpq|lpr|lprm|lpstat|ls|lsmod|lsof|lzcat|lzma|mach|mail|mailcompat|mailx|make|man|merge|mesg|mii-tool|mkdir|mkfs|mkswap|modinfo|modprobe|more|mount|mt|mv|myisamchk|mysql|mysqldump|nc|neqn|netstat|newalias|newform|newgrp|nice|niscat|nischmod|nischown|nischttl|nisdefaults|nisgrep|nismatch|nispasswd|nistbladm|nl|nmap|nohup|nroff|nslookup|od|on|onintr|optisa|pack|pagesize|parted|partprobe|passwd|paste|pax|pcat|perl|pg|pgrep|pico|pine|ping|pkill|poweroff|pr|printenv|printf|priocntl|ps|pstree|pvs|pwd|quit|rcp|readlink|reboot|red|rehash|rename|renice|repeat|replace|rgview rgvim|rlogin|rm|rmdir|rmmod|rn|route|rpcinfo|rsh|rsync|rview|rvim|s2p|sag|sar|scp|screen|script|sdiff|sed|sendmail|service|set|setenv|setfacl|sfdisk|sftp|sh|shred|shutdown|sleep|slogin|smbclient|sort|spell|split|startx|stat|stop|strftime|strip|stty|su|sudo|swapoff|swapon|sysklogd|tabs|tac|tail|talk|tar|tbl|tcopy|tcpdump|tcsh|tee|telinit|telnet|test|time|timex|todos|top|touch|tput|tr|traceroute|trap|tree|troff|tty|ul|umask|umount|unalias|uname|uncompress|unhash|uniq|unlink|unlzma|unpack|until|unxz|unzip|uptime|useradd|userdel|usermod|vacation|vgrind|vi|view|vim|vipw|visudo|vmstat|w|wait|wall|wc|wget|whatis|whereis|which|while|who|whoami|whois|write|X|Xorg|xargs|xfd|xhost|xinit|xlsfonts|xrdb|xset|xterm|xz|xzcat|yacc|yes|yppasswd|yum|zcat|zip|zipcloak|zipinfo|zipnote|zipsplit) -{1,2}\w+ \w*')
pattern43 = re.compile('(?:https|http)://\w*\S*\d*', re.DOTALL)
#pattern27 = re.compile(r'(?: |^)[a-zA-Z]+', re.DOTALL)
#pattern20 = re.compile(r'.*?({{.*?}}).*?', re.DOTALL)
#pattern21 = re.compile(r'.*?({code.*?{code}).*?', re.DOTALL)
#pattern22 = re.compile(r'.*?({noformat.*?{noformat}).*?', re.DOTALL)
#pattern23 = re.compile(r'.*?({panel.*?{panel}).*?', re.DOTALL)
#pattern24 = re.compile(r'.*?({quote.*?{quote}).*?', re.DOTALL)
#pattern25 = re.compile(r'\(\d{2}:.*?\n', re.DOTALL)
################################################################
################################################################



arr_patterns = [pattern0, pattern1, pattern2, pattern3, pattern4, pattern5, pattern6, pattern7, pattern8, pattern9, pattern10, pattern11, pattern12, pattern13, pattern14, pattern15, pattern16, pattern17, pattern18, pattern19, pattern20, pattern21, pattern22, pattern23, pattern24, pattern25, pattern26, pattern27, pattern28, pattern29, pattern30, pattern31, pattern32, pattern33, pattern34, pattern35, pattern36, pattern37, pattern38, pattern39, pattern40, pattern41, pattern42, pattern43]


number_of_bug_descr = list()
list_of_all_projects_cleaned_bugs_descriptions_with_stack_trace_flags = list()

for i in range(1,4):
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
    list_of_bugs_descriptions_and_stack_trace_flags = [list(x) for x in subset.values]
#   
    for k,item in enumerate(list_of_bugs_descriptions_and_stack_trace_flags):
#        if k < 344:
#            continue
#        if k == 380:
#            print('|||||||||||||||||||||||||||||||||||||||||||')
#            print('|||||||||||||||||||||||||||||||||||||||||||')
#            print('|||||||||||||||||||||||||||||||||||||||||||')
#            print('|||||||||||||||||||||||||||||||||||||||||||')
#            print('|||||||||||||||||||||||||||||||||||||||||||')
#            print('|||||||||||||||||||||||||||||||||||||||||||')
#            print('|||||||||||||||||||||||||||||||||||||||||||')
#            print('|||||||||||||||||||||||||||||||||||||||||||')
#            print('|||||||||||||||||||||||||||||||||||||||||||')
#            print('|||||||||||||||||||||||||||||||||||||||||||')
#            break
#        print('|||||||||||NUMBER OF TEXT||||||||||||')
#        print(k)
#        print('|||||||||||NUMBER OF TEXT||||||||||||')
#        print()
        text = item[0]
#        print('|||||||||||||||||||||||||||||||BEGIN TEXT with trash|||||||||||||||||||||||||||')
#        print(text)
#        print('|||||||||||||||||||||||||||||||END TEXT with trash|||||||||||||||||||||||||||')
#        print()
#        print()
        list_of_bugs_descriptions_and_stack_trace_flags[k] = filter_pattern(arr_patterns, text)  
    list_of_all_projects_cleaned_bugs_descriptions_with_stack_trace_flags = list_of_all_projects_cleaned_bugs_descriptions_with_stack_trace_flags + list_of_bugs_descriptions_and_stack_trace_flags
#        print('-------------------THIS IS THE END-----------------------')
    str_for_print = 'Number of descriptions in %d project: ' % i
    print(str_for_print)
    print(len(list_of_bugs_descriptions_and_stack_trace_flags))


#print(list_of_all_projects_cleaned_bugs_descriptions_with_stack_trace_flags)
print('Number of all descriptions: ')
print(len(list_of_all_projects_cleaned_bugs_descriptions_with_stack_trace_flags))
#print(list_of_all_projects_cleaned_bugs_descriptions_with_stack_trace_flags)

##########################################################
##########################################################
#return tokens without stop words
def delete_stop_words_from_text(file_text):
    #firstly let's apply nltk tokenization 
    tokens = nltk.word_tokenize(file_text) 

    #let's delete punctuation symbols 
    tokens = [i for i in tokens if ( i not in string.punctuation )] 
    
    #deleting stop_words 
    stop_words = stopwords.words('english') 
    tokens = [i for i in tokens if ( i not in stop_words )] 
    
    #cleaning words 
    tokens = [i.replace("«", "").replace("»", "") for i in tokens] 

    #return tokens without stop words
    return tokens 

def get_tokens(file_text):  
    return delete_stop_words_from_text(file_text)

def get_bigrams(file_text):
    tokens = delete_stop_words_from_text(file_text)
    return list(ngrams(tokens,2))

def get_ngrams(file_text, n):
    tokens = delete_stop_words_from_text(file_text)
    return list(ngrams(tokens,n))

##########################################################
##########################################################
             
list_tokens_with_stack_trace_flag = [[get_tokens(x[0]),x[1]] for x in list_of_all_projects_cleaned_bugs_descriptions_with_stack_trace_flags ]
list_bigrams_with_stack_trace_flag = [[get_bigrams(x[0]),x[1]] for x in list_of_all_projects_cleaned_bugs_descriptions_with_stack_trace_flags ] 
#print(list_tokens_with_stack_trace_flag)
#print(list_bigrams_with_stack_trace_flag) 
   
thefile_words = open('F:\\mygit\\words.txt', 'w', encoding='utf-8')
for item in list_tokens_with_stack_trace_flag:
    temp_str = ', '.join(item[0])
    thefile_words.write("%r\n" % temp_str)
    thefile_words.write("%s\n" % str(item[1]))
thefile_words.close()

thefile_bigrams = open('F:\\mygit\\bigrams.txt', 'w', encoding='utf-8')
for item in list_bigrams_with_stack_trace_flag:
    my_str = ' '
    for x in item[0]:
        temp_str = ' / '.join(x)
        my_str = my_str + ' , ' + temp_str
    thefile_bigrams.write("%r\n" % my_str)
    thefile_bigrams.write("%s\n" % str(item[1]))
thefile_bigrams.close()