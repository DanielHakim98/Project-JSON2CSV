import sys
import os

current_path = os.path.dirname(os.path.realpath(__file__))
parent_path = os.path.dirname(current_path)
sys.path.append(parent_path)

from main.json_2_csv import *

def test_get_json():
  assert type(get_json()) == dict or type(get_json()) == list,\
  "Test failed because returned object is neither Dictionary nor List."

def test_get_keys():
  sample_json = [
    {"name": "Tom", "age": 10},
    {"name": "Mark", "age": 5, "height":4},
    {"name": "Pam", "age": 7, "weight":90}
  ]

  assert(get_keys(sample_json)) == ["name", "age", "height","weight"]
  assert(type(get_keys())) == list,"Test failed because returned keys is not in a list."