import pandas as pd
import numpy as np
from datetime import datetime
import sys
import os

def validate_inference_data(df):
    col_names = ['amount','grade','years','ownership','income','age']
    num_cols = len(col_names)
    flag = True
    for name in df.columns:
        if name not in col_names:
            flag = False
            break
    if num_cols!=df.shape[1]:
        flag = False
    return flag

def validate_levels_cat(df):
    grade_validation = ['A','B','C','D','E','F','G']
    ownership_validation = ['MORTGAGE','OTHER','OWN','RENT']
    g_val = False
    o_val = False
    if set(df['grade'].unique()) == set(grade_validation):
        g_val = True
    if set(df['ownership'].unique()) == set(ownership_validation):
        o_val = True
    if g_val and o_val:
        return True
    else:
        return False

def create_x(df):
    df = df.dropna()
    X = pd.get_dummies(df).values
    return X

def get_summary_stats(X):
    return pd.DataFrame(X).describe()

def get_timestamp():
    now = datetime.now()
    y = now.year
    m = now.month
    d = now.day
    hour = now.hour
    minute = now.minute
    sec = now.second
    timestamp = f'{y}_{m}_{d}_{hour}_{minute}_{sec}'
    return timestamp

def save_inference_data(X,summary_stats):
    timestamp = get_timestamp()
    path_dir = f"../assets/inference/{timestamp}"
    if not os.path.exists(path_dir):
        os.mkdir(path_dir)
    path_file = os.path.join(path_dir,"X")
    path_summary = os.path.join(path_dir,"summary.csv")
    np.save(path_file,X)
    summary_stats.to_csv(path_summary)
    print("Inference and summary file saved")
    

if __name__=="__main__":
    path_infer_file = sys.argv[1]
    df = pd.read_csv(path_infer_file)
    if validate_inference_data(df) and validate_levels_cat(df):
        X = create_x(df)
        summary = get_summary_stats(X)
        save_inference_data(X,summary)
    else:
        print("Failed to validate inference data, check the raw data")