import re
import sys
import string
import pickle
import tempfile
from random import shuffle
from string import punctuation

arg2 = sys.argv[2]
classavg = {}
classes = {}
new_list = []


fl = tempfile.TemporaryFile(mode='w+')
arg1 = sys.argv[1]

with open(arg1, 'r', errors = 'ignore') as f:
     for line in f:
         word = line.split()
         lt = len(word)
         for i in range(lt):
             if lt >= 2:
                 if i == 0:
                     ss = word[i].split('/')[1]+" "+'w:'+word[i].split('/')[0]+" "+'wprev:'+'startpos'+" "+'wnext:'+word[i+1].split('/')[0]
                     fl.write(ss)
                     fl.write('\n')
                 elif i == lt-1:
                     ss = word[i].split('/')[1]+" "+'w:'+word[i].split('/')[0]+" "+'wprev:'+word[i-1].split('/')[0]+" "+'wnext:'+'endpos'
                     fl.write(ss)
                     fl.write('\n')
                 else:
                     ss = word[i].split('/')[1]+" "+'w:'+word[i].split('/')[0]+" "+'wprev:'+word[i-1].split('/')[0]+" "+'wnext:'+word[i+1].split('/')[0]
                     fl.write(ss)
                     fl.write('\n')
             else:
                 ss = word[i].split('/')[1]+" "+'w:'+word[i].split('/')[0]+" "+'wprev:'+'startpos'+" "+'wnext:'+'endpos'
                 fl.write(ss)
                 fl.write('\n')

def training():

    
    
    voc = {}
    
    fl.seek(0)
    for line in fl:
        #print(line)
        word = line.split()
        if word[0] not in new_list:
            new_list.append(word[0])
        if word[0] not in classes.keys():
            classes[word[0]] = {}
        for e_word in word[1:]:
            voc[e_word] = 0

    for cls in new_list:
        classes[cls] = dict(voc)
    for cls in new_list:
        classavg[cls] = dict(voc)

    print(len(new_list))
    #print(voc)
    #print(classes)
    #print(new_list)

    f.close()

    for i in range(19):
        n = 0
        m = 0

        fl.seek(0)
        r = fl.readlines()
        shuffle(r)
        for line in r:
            m += 1
            wrds = line.split()
            aclass = wrds[0]
            fea = wrds[1:]
            pclass = pred(fea)
            if aclass != pclass:
                n += 1
                for eword in wrds[1:]:
                    classes[aclass][eword] += 1
                    classes[pclass][eword] -= 1

        k = float(n/m)
        print(m)
        print(n)
        print('iteration:{} error:{}'.format(i,k))    
        f.close()
        for cls in new_list:
            for word in classavg[cls]:
                classavg[cls][word] += classes[cls][word]

    with open(arg2, 'wb') as ft:
        pickle.dump(classavg, ft, protocol=0)   
    #print(classes)

def pred(lines) :
    tot = {}
    for cls in new_list:
        tot[cls] = 0
        for wd in lines:
            tot[cls] += classes[cls][wd]
    m=float('-inf')

    for cls in new_list:
        if tot[cls] >= m:
            m = tot[cls]
            pclass = cls
    return pclass

training()





 

