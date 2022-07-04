import json
import sys
import os

current_path = os.path.dirname(os.path.realpath(__file__))
parent_path = os.path.dirname(current_path)
sys.path.append(parent_path)

def get_json(json_path):
  with open(json_path) as f:
    json_data = json.load(f)
  return json_data

def get_keys(obj):
  if type(obj) == list:
    keys = set()
    for item in obj:
      keys.update(item.keys())
      #ALT METHOD:
      # keys = set().union(*(d.keys() for d in sample))
    return list(keys)
  else:
    return obj.keys()





