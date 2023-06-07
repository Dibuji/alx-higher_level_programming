#!/usr/bin/python3
def islower(c):
    value = ord(c)
    for i in range(97, 123):
        if value == i:
            return True
    return False
