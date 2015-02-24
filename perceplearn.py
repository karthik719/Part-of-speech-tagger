import re
import sys
import string
import pickle
from random import shuffle
from string import punctuation

arg2 = sys.argv[2]
classavg = {}
classes = {}
new_list = []

def training():

    arg1 = sys.argv[1]
    
    voc = {}
    

    with open(arg1, 'r', errors='ignore') as f:
        for line in f:
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

    for i in range(12):
        n = 0
        m = 0
        with open(arg1, 'r') as f:
            r = f.readlines()
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





 

