import sys
import os

current_path = os.path.dirname(os.path.realpath(__file__))
parent_path = os.path.dirname(current_path)
sys.path.append(parent_path)

from main.json_2_csv import *

def test_get_json():
  json_path = parent_path + '/sample/sample2.json'
  assert type(get_json(json_path)) == dict or type(get_json()) == list,\
    "Returned object is neither Dictionary nor List."

sample_json =\
[
    {"name": "Tom", "age": 10},
    {"name": "Mark", "age": 5, "height":4},
    {"name": "Pam", "age": 7, "weight":90}
]

def test_get_keys():
  keys_from_json = get_keys(sample_json)
  assert(set(keys_from_json)) ==set(["name","age","weight","height"]),\
    "Keys retrieved are not the same as expected."

def test_returned_keys_are_list():
  keys_from_json = get_keys(sample_json)
  assert(type(keys_from_json)) == list,\
    "Returned keys is not in a list."