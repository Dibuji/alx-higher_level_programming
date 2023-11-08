#!/usr/bin/python3
import json
"""Module that defines Function to return JSON Representation of an object"""


def to_json_string(my_obj):
    """Function to return JSON representation of an object (string)"""

    return json.dumps(my_obj)
