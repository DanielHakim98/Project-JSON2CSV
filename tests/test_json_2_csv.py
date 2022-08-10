import sys
import os

current_path = os.path.dirname(os.path.realpath(__file__))
parent_path = os.path.dirname(current_path)
sys.path.append(parent_path)

from main.json_2_csv import *



sample_json =\
[
    {"name": "Tom", "age": 10},
    {"name": "Mark", "age": 5, "height":4},
    {"name": "Pam", "age": 7, "weight":90}
]

def test_get_json():
    json_path = parent_path + '/sample/sample2.json'
    assert type(get_json(json_path)) == dict \
        or type(get_json()) == list,\
    "Returned object is neither Dictionary nor List."

def test_csv_header():
    assert detect_csv_header(sample_json) == ['name','age','height','weight'],\
        "Does not equal expected list of columns"

sample_csv_data = [
    'name,age,height,weight',
    '"Tom","10","",""',
    '"Mark","5","4",""',
    '"Pam","7","","90"'
]

def test_convert_to_csv():
    header = detect_csv_header(sample_json)
    csv_data = convert_to_csv(sample_json,header)
    assert csv_data == sample_csv_data