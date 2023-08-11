#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    number = (len(sys.argv))
    total = 0

    i = 1
    while i < number:
        total = total + int(sys.argv[i])
        i = i + 1

    print("{}".format(total))
