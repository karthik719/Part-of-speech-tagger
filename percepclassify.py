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


for line in sys.stdin:
    word = line.split()
    tot = {}
    for cls in new_list:
        tot[cls] = 0
        for wd in word:
            if wd in classes[cls]:
                tot[cls] += classes[cls][wd]
    m = float('-inf')
    #print(tot)

    for cls in new_list:
        if tot[cls] > m:
            m = tot[cls]
            pclass = cls
    print(pclass)




