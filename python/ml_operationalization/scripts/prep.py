import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import sys

def create_xy(df):
    df = df.dropna()
    df = pd.get_dummies(df)
    X=df.drop('default',axis=1).values
    y=df['default'].values
    return X,y

def get_train_test_split(X,y):
    X_train,X_test,y_train,y_test = train_test_split(X,y,train_size=0.80,random_state=200)
    return {'X_train':X_train,'X_test':X_test,'y_train':y_train,'y_test':y_test}
    
def save_data(**data):
    for name in data:
        val = data[name]
        np.save(f'../assets/data/{name}',val)
    
if __name__=="__main__":
    path = sys.argv[1]
    df = pd.read_csv(path)
    X,y = create_xy(df)
    data = get_train_test_split(X,y)
    print("Saving the data after processing")
    save_data(**data)
    print("Data Saved")