#!/usr/bin/python3
def add_tuple(tup_a=(), tup_b=()):
    """Adds 2 tuples"""

    if len(tup_a) == 0:
        new_tuple_a = (0, 0)
    elif len(tup_a) == 1:
        new_tuple_a = (tup_a[0], 0)
    else:
        new_tuple_a = (tup_a[0], tup_a[1])

    if len(tup_b) == 0:
        new_tuple_b = (0, 0)
    elif len(tup_b) == 1:
        new_tuple_b = (tup_b[0], 0)
    else:
        new_tuple_b = (tup_b[0], tup_b[1])

    new_tup = (new_tuple_a[0] + new_tuple_b[0],
               new_tuple_a[1] + new_tuple_b[1])
    return new_tup
