import re
import sys
import string
import pickle
import codecs
from string import punctuation


arg1 = sys.argv[1]
new_list = []
with open(arg1 , 'rb') as fk:
    classes = pickle.load(fk)
new_list=classes.keys()


sys.stdin = codecs.getreader('utf8')(sys.stdin.detach(), errors='ignore')
for line in sys.stdin:
    word = line.split()
    lt = len(word)
    st = ''
    for i in range(lt):
        ss = []
        if lt >= 2:
            if i == 0:
                ss.append('w:'+word[i])
                ss.append('wprev:'+'startpos')
                ss.append('wnext:'+word[i+1])    
            elif i == lt-1:
                ss.append('w:'+word[i])
                ss.append('wprev:'+word[i-1])
                ss.append('wnext:'+'endpos')
                    
            else:
                ss.append('w:'+word[i])
                ss.append('wprev:'+word[i-1])
                ss.append('wnext:'+word[i+1])
                     
        else:
             ss.append('w:'+word[i])
             ss.append('wprev:'+'startpos')
             ss.append('wnext:'+'endpos')     
    
        tot = {}
        for cls in new_list:
            tot[cls] = 0
            for wd in ss:
                if wd in classes[cls]:
                    tot[cls] += classes[cls][wd]
        m = float('-inf')
        #print(tot)

        for cls in new_list:
            if tot[cls] >= m:
                m = tot[cls]
                pclass = cls
        st += word[i]+"/"+pclass+" "
    print(st)






