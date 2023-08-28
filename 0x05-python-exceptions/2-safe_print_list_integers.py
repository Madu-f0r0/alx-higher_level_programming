#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """ Prints the first x elements of a list and only integers """

    try:
        int_no = 0
        for i in range(x):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                int_no += 1
        print()
        return int_no
    except IndexError:
        raise
