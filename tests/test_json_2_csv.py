import sys
import os

current_path = os.path.dirname(os.path.realpath(__file__))
parent_path = os.path.dirname(current_path)
sys.path.append(parent_path)

from main.json_2_csv import *

#for sample1.json
def test_1_get_json():
    json_path = parent_path + '/sample/sample1.json'
    assert type(get_json(json_path)) == dict \
        or type(get_json(json_path)) == list,\
    "Returned object is neither Dictionary nor List."
#for sample2.json
def test_2_get_json():
    json_path = parent_path + '/sample/sample2.json'
    assert type(get_json(json_path)) == dict \
        or type(get_json(json_path)) == list,\
    "Returned object is neither Dictionary nor List."

#for sample1.json
def test_1_csv_header():
    json_path = parent_path + '/sample/sample1.json'
    json_data = get_json(json_path)
    assert detect_csv_header(json_data) == ['Id','UserName'],\
        "Does not equal expected list of columns"
#for sample2.json
def test_2_csv_header():
    json_path = parent_path + '/sample/sample2.json'
    json_data = get_json(json_path)
    assert detect_csv_header(json_data) == ['Id','UserName','email','Country','Job'],\
        "Does not equal expected list of columns"

sample_1_csv_data = [
    'Id,UserName',
    '"1","Sam Smith"',
    '"2","Samsonite"',
    '"3","Sammy"',
]
def test_1_convert_to_csv():
    json_path = parent_path + '/sample/sample1.json'
    json_data = get_json(json_path)
    header = detect_csv_header(json_data)
    csv_data = convert_to_csv(json_data,header)
    assert csv_data == sample_1_csv_data

sample_2_csv_data = [
    'Id,UserName,email,Country,Job',
    '"1","Sam Smith","sam.smith@gmail.com","UK","Singer"',
]
def test_2_convert_to_csv():
    json_path = parent_path + '/sample/sample2.json'
    json_data = get_json(json_path)
    header = detect_csv_header(json_data)
    csv_data = convert_to_csv(json_data,header)
    assert csv_data == sample_2_csv_data

sample_json =\
[
    {"name": "Tom", "age": 10},
    {"name": "Mark", "age": 5, "height":4},
    {"name": "Pam", "age": 7, "weight":90}
]
sample_3_csv_data = [
    'name,age,height,weight',
    '"Tom","10","",""',
    '"Mark","5","4",""',
    '"Pam","7","","90"'
]
def test_3_convert_to_csv():
    header = detect_csv_header(sample_json)
    csv_data = convert_to_csv(sample_json,header)
    assert csv_data == sample_3_csv_data