import argparse 
parser = argparse.ArgumentParser(description = 'Summarize the results in admission files')
parser.add_argument('--files',nargs="+",help = "path of the files to be processed")
parser.add_argument('--indices',nargs = "+", help = 'index of the column to be summarized')

def compute_average_many(file_names,col_idxs):
    result = []
    for arg,col_idx in zip(file_names,col_idxs):
        with open(arg,'r') as f:
            data = f.readlines()
        all_values = []
        for row in data[1:]:
            vals = row.split(",")
            all_values.append(float(vals[int(col_idx)]))
        result.append(sum(all_values)/len(all_values))
    return result

if __name__=="__main__":
    args = parser.parse_args()
    result = compute_average_many(args.files,args.indices)
    print(result)
