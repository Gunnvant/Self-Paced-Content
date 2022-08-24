'''
Demo for testing functions
'''
import csv

def get_data(path:str,delim:str)->list:
    with open(path,"r") as f:
        reader = csv.DictReader(f,delimiter=delim)
        data = []
        for row in reader:
            data.append(row)
    return data
