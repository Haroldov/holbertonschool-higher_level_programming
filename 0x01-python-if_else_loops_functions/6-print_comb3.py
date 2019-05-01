#!/usr/bin/python3
str = ", "
for unit in range(10):
    if unit == 8:
        str = "\n"
    for tens in range(unit + 1, 10):
        print("{}{}".format(unit, tens), end=str)
