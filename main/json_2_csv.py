import json
import sys
import os
import re
import pdb

current_path = os.path.dirname(os.path.realpath(__file__))
parent_path = os.path.dirname(current_path)
sys.path.append(parent_path)

def get_json(json_path):
    with open(json_path) as f:
        json_data = json.load(f)
    return json_data

sample_json =\
[
    {"name": "Tom", "age": 10},
    {"name": "Mark", "age": 5, "height":4},
    {"name": "Pam", "age": 7, "weight":90}
]

def detect_csv_header(input):
    all_keys = []
    if isinstance(input,list):
        # Collect all existing keys (including duplicates)
        for item in input:
            for key,_value in item.items():
                all_keys.append(key)
        header = []
        # Filter duplicate keys
        while(len(all_keys)>0):
            temp = all_keys.pop(0)
            if temp not in header:
                header.append(temp)
        return header
    else:
        for key,_value in input.items():
            all_keys.append(key)
        return all_keys

def convert_to_csv(data,header):
    str_header = ""
    all_rows = []

    # Convert list of columns (header) to string
    for idx,ele in enumerate(header):
        str_header += str(ele)
        #Concatenate ',' if it's not the end of the row
        if idx < len(header)-1:
            str_header += ','
    all_rows.append(str_header)

    # Collect data from dictionary and make it into list of header + rows
    for idx,item in enumerate(data):
        out_str = ""
        # Extract row value with respect to its column name
        for idx,value in enumerate(header):
            out_str += '"'+ str(item.get(value)) + '"'
            # Concatenate ',' if it's not the end of row
            if idx < len(header)-1:
                out_str += ','
        out_str = out_str.replace("None", "")
        all_rows.append(out_str)
    return all_rows

def save_to_csv(data,newline = True):
    output_dir = os.path.join(os.getcwd(),'data','output')
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_dir_abs = os.path.join(output_dir,'output.csv')
    with open(output_dir_abs, 'w') as writer:
        eol = '\n' if newline == True else ''
        for row in data:
            writer.write(row + eol)

# Just for testing!
# csv_data = convert_to_csv(sample_json,detect_csv_header(sample_json))
# save_to_csv(csv_data)
