#!/usr/bin/python3
"""Defines a function that adds all arguments to a python list,
    and then saves them to a file
"""
import json
import sys
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


file = "add_item.json"

if not os.path.exists(file):
    my_list = []
else:
    my_list = list(load_from_json_file(file))

n = len(sys.argv)

for i in range(1, n):
    my_list.append(sys.argv[i])

save_to_json_file(my_list, file)
