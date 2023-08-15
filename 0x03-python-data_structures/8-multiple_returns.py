#!/usr/bin/python3
def multiple_returns(sentence):
    """Returns a tuple containing the length of a string

    and its first character"""

    if sentence == "":
        first_chr = None
    else:
        first_chr = sentence[0]
    new_tuple = (len(sentence), first_chr)
    return new_tuple
