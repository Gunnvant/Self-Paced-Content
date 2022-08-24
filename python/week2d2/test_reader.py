import pytest 
import reader
import os 
IO = reader.IO()
path_csv = "addresses.csv"

def test_read_type():

    res = IO.read_csv(path_csv)
    assert type(res)==list 

def test_rows_returned():
    res = IO.read_csv(path_csv)
    assert len(res) == 21

def test_json_exists():
    path_write = "test.json"
    res = IO.read_csv(path_csv)
    IO.write_json(res,path_write)
    os.path.exists(path_write)
