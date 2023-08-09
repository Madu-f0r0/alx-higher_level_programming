#!/usr/bin/python3
def add(a, b):
    """adds two integers and returns the result"""
    if not isinstance(a, int) or not isinstance(b, int):
        return TypeError
    return a + b
