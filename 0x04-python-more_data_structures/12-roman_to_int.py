#!/usr/bin/python3
def roman_to_int(roman_string):
    """Converts a roman numeral to an integer"""
    roman_dict = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10,
                  "V": 5, "I": 1}

    if roman_string is None:
        return 0

    latin_num = 0
    for i in range(len(roman_string)):
        if roman_string[i] not in list(roman_dict):
            return 0
        if (i != len(roman_string) - 1 and roman_dict[roman_string[i + 1]]
                > roman_dict[roman_string[i]]):
            act_digit = roman_dict[roman_string[i + 1]]
            - roman_dict[roman_string[i]]

            latin_num += act_digit - roman_dict[roman_string[i + 1]]
        else:
            latin_num += roman_dict[roman_string[i]]

    return latin_num
