import pandas as pd
import numpy as np
from joblib import load
import os
import sys

def load_model():
    return load('../assets/model/tree.joblib')

def load_data(dir_path):
    path = os.path.join(dir_path,'X.npy')
    return np.load(path)

def get_prediction(X,clf):
    preds = clf.predict(X)
    return pd.DataFrame({'preds':preds})

def save_predictions(dir_path,preds):
    path = os.path.join(dir_path,'predictions.csv')
    preds.to_csv(path)
    print('Saved predictions')

    
if __name__=="__main__":
    dir_path = sys.argv[1]
    clf = load_model()
    X = load_data(dir_path)
    preds = get_prediction(X,clf)
    save_predictions(dir_path,preds)