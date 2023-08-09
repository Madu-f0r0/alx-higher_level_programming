#!/usr/bin/python3
def print_last_digit(number):
    lastNum = int(str(number)[-1])

    print("{:d}".format(lastNum), end="")
    return lastNum
