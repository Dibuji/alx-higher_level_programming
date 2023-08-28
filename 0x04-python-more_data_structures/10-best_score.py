#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None

    comp_keys = list(a_dictionary)

    larger = comp_keys[0]
    for key in comp_keys:
        if a_dictionary.get(key) > a_dictionary.get(larger):
            larger = key
    return larger
