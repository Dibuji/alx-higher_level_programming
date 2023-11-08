#!/usr/bin/python3
"""Module that defines Function to return JSON Representation of an object"""
import json


def to_json_string(my_obj):
    """Function to return JSON representation of an object (string)"""

    return json.dumps(my_obj)
