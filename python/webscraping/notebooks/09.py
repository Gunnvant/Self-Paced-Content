from multiprocessing import Pool, cpu_count
from bs4 import BeautifulSoup
import os
import time

def process_html(name):
    base_path = "../html_data"
    path = os.path.join(base_path,name)
    with open(path,'r') as f:
        html = f.read()
    soup = BeautifulSoup(html,'html.parser')
    title = soup.title.text.strip()
    name = name.replace('html','txt').replace("-","_")
    try:
        with open(name,'w') as f:
            f.write(title)
    except:
        print(f"{name} could not be written. Its content is {title}")

if __name__=="__main__":
    base_path = "../html_data"
    file_names = os.listdir(base_path)
    file_names = [x for x in file_names if x.endswith("html")]
    start = time.time()
    with Pool(processes=cpu_count()) as p:
        p.map(process_html,file_names)
    end = time.time()
    print(end-start)