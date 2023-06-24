import pandas as pd
from bs4 import BeautifulSoup
import sys
import os
dir_read = "./raw_html"
dir_write = "./csv"

if __name__=="__main__":
    '''
    scrapper.py file_html file_csv
    '''
    path_read = os.path.join(dir_read,sys.argv[1])
    path_write = os.path.join(dir_write,sys.argv[2])
    with open(path_read,'r') as f:
        html = f.read()
    s = BeautifulSoup(html,'html.parser')
    headers = [x.text.strip() for x in s.find('thead').find("tr").find_all("th")]
    values = []
    for row in s.find('tbody').find_all("tr"):
        v = [x.text.strip() for x in row.find_all("td")]
        values.append(v)
    table = pd.DataFrame(values,columns=headers)
    table.to_csv(path_write,index=False)
    