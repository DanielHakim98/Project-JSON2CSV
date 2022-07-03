import json
import sys
import os
from xml.dom.minidom import Element

current_path = os.path.dirname(os.path.realpath(__file__))
parent_path = os.path.dirname(current_path)
sys.path.append(parent_path)

def get_json():
  json_path = parent_path + '/sample/sample1.json'
  print(json_path)
  with open(json_path) as f:
    d = json.load(f)
    print(d)
    print(type(d))
  return d

