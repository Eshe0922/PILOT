import gzip
import os
import json
import numpy as np
from more_itertools import chunked

DATASET_DIR='./data_preprocessed/Devign'
DATA_DIR='./data_raw/Devign'

def format_str(string):
    for char in ['\r\n', '\r', '\n']:
        string = string.replace(char, ' ')
    return string

def preprocess_train_data():

    print("start processing")
    print("start processing train data")

    path_train = os.path.join(DATASET_DIR, 'train.json')
    data_train = []
    
    with open(path_train, "r", encoding='utf-8') as pf:
        for line in pf.readlines():
            dic = json.loads(line)
            data_train.append(dic)
    idxs = np.arange(len(data_train))
    data_train = np.array(data_train, dtype=np.object)

    data_train = data_train[idxs]
    examples_train = []
    cnt_0 = 0
    cnt_1 = 0
    for index in data_train:
        temp = str(index['func'])
        temp = format_str(temp)
    
        example = (str(index['target']),index['commit_id'],temp)
        example = '<CODESPLIT>'.join(example)
        examples_train.append(example)

        if index['target'] == 0:
            cnt_0 += 1
        elif index['target'] == 1:
            cnt_1 += 1

    print(cnt_0)
    print(cnt_1)
    
    file_path_train = os.path.join(DATA_DIR, 'train.txt')
    print(len(examples_train))
    with open(file_path_train, 'w', encoding='utf-8') as f:
        f.writelines('\n'.join(examples_train))

def preprocess_eval_data():

    print("start processing eval data")
    path_eval = os.path.join(DATASET_DIR, 'valid.json')
    data_eval = []

    with open(path_eval, "r", encoding='utf-8') as pf:
        for line in pf.readlines():
            dic = json.loads(line)
            data_eval.append(dic)
 
    idxs = np.arange(len(data_eval))
    data_eval = np.array(data_eval, dtype=np.object)
    data_eval = data_eval[idxs]

    cnt_0 = 0
    cnt_1 = 0

    examples_eval = []
    for index in data_eval:
        temp = str(index['func'])
        temp = format_str(temp)
        example = (str(0),index['commit_id'],temp)
        example = '<CODESPLIT>'.join(example)
        examples_eval.append(example)

        if index['target'] == 0:
            cnt_0 += 1
        elif index['target'] == 1:
            cnt_1 += 1

    print(cnt_0)
    print(cnt_1)

    file_path_eval = os.path.join(DATA_DIR, 'valid.txt')
    print(len(examples_eval))
    with open(file_path_eval, 'w', encoding='utf-8') as f:
        f.writelines('\n'.join(examples_eval))

def preprocess_test_data():

    print("start processing")
    print("start processing test data")

    path_test = os.path.join(DATASET_DIR, 'test.jsonl')
    
    data_test = []

    with open(path_test, "r", encoding='utf-8') as pf:
        for line in pf.readlines():
            dic = json.loads(line)
            data_test.append(dic)

    idxs = np.arange(len(data_test))
    data_test = np.array(data_test, dtype=np.object)
    data_test = data_test[idxs]

    examples_test = []
    cnt_0 = 0
    cnt_1 = 0
    for index in data_test:
        temp = str(index['func'])
        temp = format_str(temp)
        
        if index['target'] == 0:
            cnt_0 += 1
        elif index['target'] == 1:
            cnt_1 += 1
      
        example = (str(0),index['commit_id'],temp)
        example = '<CODESPLIT>'.join(example)
        examples_test.append(example)

    print(cnt_0)
    print(cnt_1)

    file_path_test = os.path.join(DATA_DIR, 'test.txt')
    print(len(examples_test))

    with open(file_path_test, 'w', encoding='utf-8') as f:
        f.writelines('\n'.join(examples_test))

if __name__ == '__main__':
    preprocess_train_data()
    preprocess_eval_data()
    preprocess_test_data()


