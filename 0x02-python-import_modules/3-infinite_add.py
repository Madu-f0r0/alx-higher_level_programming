#!/usr/bin/python3

if __name__ == "__main__":
    """Add all the CL arguments"""
    from sys import argv

    argNum = len(argv)
    argSum = 0

    for i in range(1, argNum):
        argSum += int(argv[i])
    print(argSum)
