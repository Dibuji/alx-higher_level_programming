#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    total = 0
    try:
        for item in my_list:
            try:
                if isinstance(item, int):
                    print("{:d}".format(item), end="")
                    total += 1
                    if total == x:
                        break

            except (ValueError, TypeError):
                pass
    finally:
        print("")
    return total
