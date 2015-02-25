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
#print(classes)
new_list=classes.keys()

sys.stdout = codecs.getwriter('latin_1')(sys.stdout.detach())
sys.stdin = codecs.getreader('latin_1')(sys.stdin.detach())

for line in sys.stdin:

    word = line.split()
    lt = len(word)
    st = ''
    for i in range(lt):
        ss = []
        if lt >= 2:
            if i == 0:
                ss.append('w:'+word[i].rsplit('/',1)[0])
                ss.append('wt:'+word[i].rsplit('/',1)[1])
                ss.append('wprev:'+'startpos')
                ss.append('wpt:stag')
                ss.append('wnext:'+word[i+1].rsplit('/',1)[0]) 
                ss.append('wnt:'+word[i+1].rsplit('/',1)[1])
                ss.append('wptag:sner')
               
            elif i == lt-1:
                ss.append('w:'+word[i].rsplit('/',1)[0])
                ss.append('wt:'+word[i].rsplit('/',1)[1])
                ss.append('wprev:'+word[i-1].rsplit('/',1)[0]) 
                ss.append('wpt:'+word[i-1].rsplit('/',1)[1])
                ss.append('wnext:'+'endpos')
                ss.append('wnt:etag')
                ss.append('wptag:'+pclass)
                    
            else:
                ss.append('w:'+word[i].rsplit('/',1)[0])
                ss.append('wt:'+word[i].rsplit('/',1)[1])
                ss.append('wprev:'+word[i-1].rsplit('/',1)[0]) 
                ss.append('wpt:'+word[i-1].rsplit('/',1)[1])
                ss.append('wnext:'+word[i+1].rsplit('/',1)[0]) 
                ss.append('wnt:'+word[i+1].rsplit('/',1)[1])
                ss.append('wptag:'+pclass)
                 
        else:
             ss.append('w:'+word[i].rsplit('/',1)[0])
             ss.append('wt:'+word[i].rsplit('/',1)[1])
             ss.append('wprev:'+'startpos')
             ss.append('wpt:stag')
             ss.append('wnext:'+'endpos')
             ss.append('wnt:etag')
             ss.append('wptag:sner')
             
    
        tot = {}
        for cls in new_list:
            tot[cls] = 0
            for wd in ss:
                if wd in classes[cls]:
                    tot[cls] += classes[cls][wd]
        m = float('-inf')
        #print(tot)

        for cls in new_list:
            if tot[cls] > m:
                m = tot[cls]
                pclass = cls
        st += word[i]+"/"+pclass+" "

    print(st)







