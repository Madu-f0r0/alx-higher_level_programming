#!/usr/bin/python3
def no_c(my_string):
    """Removes characters c and C from a string"""

    new_string = my_string
    c_rem = 0

    for ch in range(len(my_string)):
        if my_string[ch] == 'c' or my_string[ch] == 'C':
            new_string = new_string[:ch - c_rem] + new_string[ch - c_rem + 1:]
            c_rem += 1
    return new_string
