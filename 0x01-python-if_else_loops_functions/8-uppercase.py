#!/usr/bin/python3
def uppercase(str):
    """Prints a string i uppercase"""
    for i in range(len(str)):
        print("{:s}".format(chr(ord(str[i]) - 32) if ord(str[i]) >= 97 and
              ord(str[i]) <= 122 else str[i]), sep="", end="")
    print()
