#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

lastDigit = int(str(number)[-1])
if number < 0:
    lastDigit *= -1

if lastDigit > 5:
    strComplete = "and is greater than 5"
else:
    if lastDigit == 0:
        strComplete = "and is 0"
    else:
        strComplete = "and is less than 6 and not 0"

print("Last digit of", number, "is", lastDigit, strComplete)
