#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

lastDigit = str(number)[-1]

if int(lastDigit) > 5:
    strComplete = "and is greater than 5"
else:
    if int(lastDigit) == 0:
        strComplete = "and is 0"
    else:
        strComplete = "and is less than 6 and not 0"

print("Last digit of", number, "is", str(number)[-1], strComplete)
