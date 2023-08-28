#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """ Prints x elements of a list """

    try:
        el = 0
        for i in range(x):
            print(my_list[i], end="")
            el += 1
        print()
    except IndexError:
        print()
        return el

    return el
