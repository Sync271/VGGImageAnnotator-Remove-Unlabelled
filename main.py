import sys
import os
import json

to_be_removed = []

lbl_file_dir = './'
try:
    os.mkdir('./Filtered_lbl')
except:
    None
out_dir = './Filtered_lbl/'

assert os.path.isdir(lbl_file_dir)
assert os.path.isdir(out_dir)

for lbl_file in os.listdir(lbl_file_dir):
    if lbl_file.endswith('.json'):
        to_be_removed = []
        with open(lbl_file, 'r') as f:
            lbls = f.read()
        lbls = json.loads(lbls)
        for l in lbls.keys():
            if '0' not in lbls[l]['regions']:
                to_be_removed.append(l)

        for lbl in to_be_removed:
            lbls.pop(lbl)
        print(lbls.keys())
        with open(out_dir+lbl_file, 'w') as out_f:
            lbls = json.dump(lbls, out_f)
