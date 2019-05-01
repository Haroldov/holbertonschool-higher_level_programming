#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = abs(number) % 10
if number < 0:
    lastDigit *= -1
if lastDigit > 5:
    str = "and is greater than 5"
elif lastDigit == 0:
    str = "and is 0"
else:
    str = "and is less than 6 and not 0"
print("Last Digit of {0:d} is {1:d} {2:s}".format(number, lastDigit, str))
