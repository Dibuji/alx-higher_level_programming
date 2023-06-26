#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    total = 0
    try:
        for item in my_list[:x]:
            try:
                if total < x:
                    print("{:d}".format(int(item)), end="")
                    total += 1
                else:
                    break
            except (ValueError, TypeError):
                pass
    except IndexError:
        raise Exception("IndexError: list index out of range")
    print("")
    return total
