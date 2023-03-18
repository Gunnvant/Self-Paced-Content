import pandas as pd
import matplotlib.pyplot as plt
import sys

def validate_table_names(df):
    col_names = ['default','amount','grade','years','ownership','income','age']
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

def create_deciles(df):
    df['amount_deciles'] = pd.qcut(df['amount'],10,labels=False)
    df['income_deciles'] = pd.qcut(df['income'],10,labels=False)
    df['age_deciles'] = pd.qcut(df['age'],10,labels=False)
    return df


def create_exploration_plots(df):
    cols = ['amount_deciles','income_deciles','age_deciles','grade','ownership']
    for col in cols:
        df.groupby(col)['default'].mean().plot()
        plt.savefig(f'../assets/exploration/{col}.pdf')
        plt.show()
        

if __name__=="__main__":
    path = sys.argv[1]
    df = pd.read_csv(path)
    if validate_table_names(df):
        print("Column names match, test passed")
    else:
        print("Column names don't match, test failed")
        
    if validate_levels_cat(df):
        print("Categorical Columns have relevant levels, test passed")
    else:
        print("Categorical Columns don't have relevant levels, test failed")
        
    df = create_deciles(df)
    
    create_exploration_plots(df)
    df.isnull().sum().to_csv("../assets/exploration/missing_vals.csv")