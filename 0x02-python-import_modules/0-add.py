#!/usr/bin/python3
if __name__ == "__main__":
    mod = __import__("add_0")

    add = mod.add
    a, b = 1, 2

    print("{} + {} = {}".format(a, b, add(a, b)))
