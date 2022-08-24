## Create a python class that can read csv files and 
# write data as either csv file or json file
import csv
import json

class IO:
    
    def read_csv(self,path):
        with open(path,"r") as f:
            reader = csv.DictReader(f,delimiter=",")
            data = [] 
            for row in reader:
                data.append(row)
        return data

    def write_json(self,data,path):
        with open(path,"w") as f:
            json.dump(data,f)