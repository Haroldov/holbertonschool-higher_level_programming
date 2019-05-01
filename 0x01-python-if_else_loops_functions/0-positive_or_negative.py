#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number < 0:
    str = "negative"
elif number > 0:
    str = "positive"
else:
    str = "zero"
print("{0:d} is {1:s}".format(number, str))
