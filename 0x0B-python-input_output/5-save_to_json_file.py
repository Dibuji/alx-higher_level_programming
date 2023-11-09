#!/usr/bin/python3

"""Defines a Function that writes an Object to a Text file (JSON)"""
import json


def save_to_json_file(my_obj, filename):
    """Function to write an object to a text file using JSON representation"""

    with open(filename, 'w', encoding="utf-8") as f:
        return json.dump(my_obj, f)
