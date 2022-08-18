import argparse

def compute_average(path:str,col_idx:int)-> float:
    with open(path,'r') as f:
        data = f.readlines()
    values = []
    for row in data[1:]:
        row_values = row.split(",")
        val = float(row_values[col_idx])
        values.append(val)
    res = sum(values)/len(values)
    return res

parser = argparse.ArgumentParser(description="This program computes the aggregate of a column in a file")
parser.add_argument("--path",help="Path of file")
parser.add_argument("--col_idx",help="Col index to be aggregated",type=int)
if __name__=="__main__":
    args = parser.parse_args()
    path = args.path
    col_idx = args.col_idx
    try:
        res = compute_average(path,col_idx)
        print(res)
    except:
        print("average was not computed")
    if "csv" in path:
        print("The file is comma separated")
    

  

    
