#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    total = (len(sys.argv)-1)
    if total == 0:
        print("{} arguments.".format(total))
    if total == 1:
        print("{} argument:".format(total))
        print("{}: {}".format(total, sys.argv[total]))
    if total > 0 and total != 1:
        print("{} arguments:".format(total))

        i = 1
        while i <= total:
            print("{}: {}".format(i, sys.argv[i]))
            i = i + 1
