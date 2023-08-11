#!/usr/bin/python3

if __name__ == "__main__":
    """List all the arguments"""

    from sys import argv

    argNum = len(argv) - 1

    print("{:d} {:s}{:s}".format(argNum, "argument"
          if argNum == 1 else "arguments", "." if argNum
          == 0 else ":"))

    for i in range(1, argNum + 1):
        print("{:d}: {:s}".format(i, argv[i]))
