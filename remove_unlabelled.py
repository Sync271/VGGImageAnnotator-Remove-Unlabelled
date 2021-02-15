'''Removes keys associated with unlabelled images from the .json files'''
import sys
import os
import json

lbl_file_dir = './'  # input folder

# creates folder to put the filtered .json files if the folder does not already exist
if os.path.exists('./Filtered'):
    None
else:
    os.mkdir('./Filtered')

out_dir = './Filtered/'  # output folder

for lbl_file in os.listdir(lbl_file_dir):  # looks for all files in the folder
    if lbl_file.endswith('.json'):  # filters json files in the folder
        to_be_removed = []  # list that will contain the name of labels to be removed
        with open(lbl_file, 'r') as f:
            lbls = f.read()
        lbls = json.loads(lbls)
        for l in lbls.keys():  # looks for all the labels in the json file
            # finds the images labels that are empty
            if '0' not in lbls[l]['regions']:
                # adds to the list of labels to be removed
                to_be_removed.append(l)

        for lbl in to_be_removed:  # finds each labels in the list to be removed
            lbls.pop(lbl)  # removes label for the dict
        with open(out_dir+lbl_file, 'w') as out_f:
            lbls = json.dump(lbls, out_f)
