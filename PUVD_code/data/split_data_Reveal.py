import gzip
import os
import json
import numpy as np
from more_itertools import chunked
import pandas as pd
from sklearn.utils import shuffle
import random
from sklearn.model_selection import train_test_split

DATASET_DIR='./data_raw'
DATA_DIR='./data_preprocessed'

def format_str(string):
    for char in ['\r\n', '\r', '\n']:
        string = string.replace(char, ' ')
    return string


def preprocess_data(path1,path2):

    print("start processing")
    datas = []
    with open(path1, "r", encoding='utf-8') as pf1:
        datas_no_vul = json.load(pf1)
    
    with open(path2, "r", encoding='utf-8') as pf2:
        datas_vul = json.load(pf2)
        
    for index in range(len(datas_no_vul)):
        code = datas_no_vul[index]['code']
        code = format_str(code)
        id = datas_no_vul[index]['hash']
        data = (str(0),str(id),code)
        data = '<CODESPLIT>'.join(data)
        datas.append(data)

    for index in range(len(datas_vul)):
        code = datas_no_vul[index]['code']
        code = format_str(code)
        id = datas_no_vul[index]['hash']
        data = (str(1),str(id),code)
        data = '<CODESPLIT>'.join(data)
        datas.append(data)

    labels1 = [0]*len(datas)
    train, valid_test, _, _ = train_test_split(datas, labels1, test_size = 0.2, random_state = 42)

    labels2 = [0]*len(valid_test)
    valid, test, _, _ = train_test_split(valid_test, labels2, test_size = 0.5, random_state = 42)

    path_train = './train.txt'
    path_valid = './valid.txt'
    path_test = './test.txt'

    cnt_0 = 0
    cnt_1 = 0
    for index in range(len(train)):
        if int(train[index][0]) == 0:
            cnt_0 += 1
        else:
            cnt_1 += 1 
    print('no vul',cnt_0)
    print('vul',cnt_1)

    cnt_0 = 0
    cnt_1 = 0
    for index in range(len(valid)):
        if int(valid[index][0]) == 0:
            cnt_0 += 1
        else:
            cnt_1 += 1 
    print('no vul',cnt_0)
    print('vul',cnt_1)

    cnt_0 = 0
    cnt_1 = 0
    for index in range(len(test)):
        if int(test[index][0]) == 0:
            cnt_0 += 1
        else:
            cnt_1 += 1 
    print('no vul',cnt_0)
    print('vul',cnt_1)

    with open(path_train, 'w', encoding='utf-8') as f1:
        f1.writelines('\n'.join(train))

    with open(path_valid, 'w', encoding='utf-8') as f2:
        f2.writelines('\n'.join(valid))

    with open(path_test, 'w', encoding='utf-8') as f3:
        f3.writelines('\n'.join(test))

if __name__ == '__main__':
        
    preprocess_data('./non-vulnerables.json','./vulnerables.json')