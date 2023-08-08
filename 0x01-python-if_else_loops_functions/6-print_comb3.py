#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if i >= j:
            continue
        elif i == 8 and j == 9:
            print("{:d}{:d}".format(i, j), sep="")
        else:
            print("{:d}{:d}".format(i, j), sep="", end=", ")
