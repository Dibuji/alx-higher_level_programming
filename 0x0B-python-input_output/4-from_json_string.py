#!/usr/bin/python3
"""defines a json string to python data structure"""
import json


def from_json_string(my_str):
    """function that converts json string to python data structure"""

    return json.loads(my_str)
