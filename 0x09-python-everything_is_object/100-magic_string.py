#!/usr/bin/python3
def magic_string():
    magic_string.count = 1 + getattr(magic_string, 'count', 0)
    return "BestSchool" + (magic_string.count - 1) * ", BestSchool"
