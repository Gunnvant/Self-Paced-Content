import pytest ## show the installation
from func import get_data
path = "breweries.csv"

def test_return_type():
    res = get_data(path,",")
    assert type(res) == list

def test_rows_returned():
    res = get_data(path,",")
    assert len(res) == 8106