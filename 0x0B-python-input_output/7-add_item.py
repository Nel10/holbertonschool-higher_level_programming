#!/usr/bin/python3
"""
script that adds all arguments to a Python list, then save to a file
"""
import json
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    json_list = load_from_json_file(filename)
except:
    json_list = []

for argu in sys.argv[1:]:
    json_list.append(argu)

save_to_json_file(json_list, filename)
