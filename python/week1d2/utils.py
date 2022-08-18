def get_average(file_path,col_idx=1):
    '''
    This function computes average of a column in a csv file
    file_path(str): path to csv file whose aggregation we need to compute
    col_idx(int): index of the column that one wants to find an average for
    '''
    with open(file_path,"r") as f:
        data = f.readlines()
    values = []
    for row in data[1:]:
        val = float(row.split(",")[col_idx])
        values.append(val)
    avg = sum(values)/len(values)
    return avg