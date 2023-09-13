#!/usr/bin/python3
"""Defines writing an object to text file"""
import json


def save_to_json_file(my_obj, filename):
    """function that writes to json file"""
    with open(filename, "w", encoding="utf-8") as f:
        return json.dump(my_obj, f)
