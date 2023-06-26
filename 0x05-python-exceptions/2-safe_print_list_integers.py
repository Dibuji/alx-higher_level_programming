#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    total = 0
    try:
        for item in my_list[:x]:
            try:
                print("{:d}".format(item), end="")
                total += 1
            except ValueError:
                pass
    except IndexError:
        raise Exception("IndexError: list index out of range")
    print("")
    return total
