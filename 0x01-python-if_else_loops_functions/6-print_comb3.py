#!/usr/bin/python3
for i in range(100):
    if i < 89:
        if (i // 10) != (i % 10):
            if (i // 10) < (i % 10):
                print("{}{}".format((i // 10), (i % 10)), end=", ")
    elif i == 89:
        print("{}".format(i))
