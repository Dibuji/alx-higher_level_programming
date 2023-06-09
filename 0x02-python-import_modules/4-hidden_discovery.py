#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    hidden = dir(hidden_4)
    hidden.sort()
    for i in hidden:
        if i[0] == "__":
            pass
        else:
            print("{}".format(i))
