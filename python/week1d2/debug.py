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
if __name__=="__main__":
    path = "admission.csv"
    col_idx = 0
    res = compute_average(path,col_idx)
    print(res)

