import pandas as pd
import os
import sys
dir_read = "./csv"
dir_write = './sql_insert'
def SQL_INSERT_STATEMENT_FROM_DATAFRAME(SOURCE, TARGET):
    template = '''INSERT INTO {target} values 
    {values}
    '''
    sql_texts = []
    for index, row in SOURCE.iterrows():
        row_values = tuple(row.values)
        row_values = [x.replace("'","\\")  if type(x)==str else x for x in row_values]       
        sql_texts.append(str(row_values))
    sql_texts = ',\n'.join(sql_texts)
    template = template.format(target=TARGET,values=sql_texts)
    template = template.replace("[","(").replace("]",")")       
    return template
if __name__=="__main__":
    '''
    python insert.py csv_file sql_file
    '''
    path_read = os.path.join(dir_read,sys.argv[1])
    path_write = os.path.join(dir_write,sys.argv[2])
    t = pd.read_csv(path_read)
    t.fillna("NULL",inplace=True)
    table = path_read.split('\\')[-1].split('.csv')[0]
    template = SQL_INSERT_STATEMENT_FROM_DATAFRAME(t,table)
    with open(path_write,'w') as f:
        f.write(template)