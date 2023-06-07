#!/usr/bin/python3
def uppercase(str):
    upper = ""
    for i in str:
        if ord(i) in range(97, 123):
            value = ord(i) - 32
            upper = upper + chr(value)
        else:
            upper = upper + i
    print("{}".format(upper))
