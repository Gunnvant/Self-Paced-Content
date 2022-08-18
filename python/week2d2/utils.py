'''
Object oriented programming basics
'''

import csv
from typing import Union

def read_csv(path:str,delim:str)->list:
    with open(path,'r') as f:
        reader = csv.DictReader(f,delimiter=delim)
        data = []
        for row in reader:
            data.append(row)
    return data

def write_csv(path:str,data:list,headers:Union[str,None]=None):
    with open(path,'w') as f:
        if headers is None:
            headers = list(data[0].keys())
        writer = csv.DictWriter(f,fieldnames=headers)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

def summary(data:list)->dict:
    n_cols = len(data[0].keys())
    n_rows = len(data)
    col_names = list(data[0].keys())
    return {'n_cols':n_cols,'n_rows':n_rows,'col_names':col_names}

def dtypes(data:list)->dict:
    row = data[1]
    schema = {}
    for k,v in row:
        if type(v)!=str:
            schema[k] = str(type(v))
        else:
            if v.isnumeric():
                schema[k] = 'num'
            else:
                schema[k] = 'str'
    return schema