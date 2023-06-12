#!/usr/bin/python3

def no_c(my_string):
    characters = ['C', 'c']
    new_string = ""

    for char in my_string:
        if char not in characters:
            new_string += char

    return new_string
