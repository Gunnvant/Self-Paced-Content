import os
import json
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, roc_auc_score
import sklearn.model_selection as model_selection
from joblib import dump, load
import sys
import numpy as np


def get_data(base_dir):
    data_file_names = [x for x in os.listdir(base_dir) if x.endswith('.npy')]
    data = {}
    for name in data_file_names:
        path_file = os.path.join(base_dir,name)
        data[name] = np.load(path_file)
    return data

def train_model(**data):
    clf=DecisionTreeClassifier(max_depth=3,random_state=200)
    mod=model_selection.GridSearchCV(clf,param_grid={'max_depth':[2,3,4,5,6]})
    mod.fit(data['X_train.npy'],data['y_train.npy'])
    m = mod.best_estimator_
    return m

def save_model(m):
    dump(m, '../assets/model/tree.joblib')
    print("Data saved")

def create_metrics(data,clf):
    y_test = data['y_test.npy']
    X_test = data['X_test.npy']
    clf_report = classification_report(y_test,clf.predict(X_test))
    auc = roc_auc_score(y_test,clf.predict_proba(X_test)[:,1])
    return {'auc':auc,'clf_report':clf_report}
    
def save_metrics(metrics):
    with open('../assets/model/metrics.json', 'w') as out_file:
        json.dump(metrics, out_file, sort_keys = True, indent = 4,
               ensure_ascii = False)
        
if __name__=="__main__":
    base_dir = sys.argv[1]
    data = get_data(base_dir)
    m = train_model(**data)
    metrics = create_metrics(data,m)
    save_model(m)
    save_metrics(metrics)