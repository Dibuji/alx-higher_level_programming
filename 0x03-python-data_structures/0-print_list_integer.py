#!/usr/bin/python3

def print_list_integer(my_list=[]):
    total = len(my_list)

    for i in range(total):
        print("{}".format(int(my_list[i])))
