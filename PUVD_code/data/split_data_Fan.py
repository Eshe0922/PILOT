import gzip
import os
import json
import jsonlines
import numpy as np
from more_itertools import chunked
import pandas as pd
from sklearn.utils import shuffle
import random

DATASET_DIR='./'
DATA_DIR='./'

def format_str(string):
    for char in ['\r\n', '\r', '\n']:
        string = string.replace(char, ' ')
    return string


def preprocess_data(path1,path2):

    print("start processing")

    datas = pd.read_csv(path1,encoding="utf-8")
    examples = []

    cnt_0 = 0
    cnt_1 = 0
    print(datas.columns)

    for index in range(len(datas)):
        temp = str(datas['func_before'][index])
        temp = format_str(temp)
 
        example = (str(datas['target'][index]),datas['commit_id'][index],temp)
        example = '<CODESPLIT>'.join(example)
        examples.append(example)

        if datas['target'][index] == 0:
            cnt_0 += 1
        elif datas['target'][index] == 1:
            cnt_1 += 1

    print(cnt_0)
    print(cnt_1)

    with open(path2, 'w', encoding='utf-8') as f1:
        f1.writelines('\n'.join(examples))

if __name__ == '__main__':

    preprocess_data('./data_raw/train.csv','./data_preprocessed/train.txt')
    preprocess_data('./data_raw/val.csv','./data_preprocessed/valid.txt')
    preprocess_data('./data_raw/test.csv','./data_preprocessed/test.txt')




