#!/usr/bin/python3
def safe_print_division(a, b):
    """ Divides 2 integers and prints the result """

    try:
        return (a / b)
    except Exception:
        return None
    finally:
        print("Inside result: {}".format(a / b if b != 0 else None))
