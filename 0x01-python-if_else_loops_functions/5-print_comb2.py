#!/usr/bin/python3
for number in range(99):
    print("{0:d}{1:d}".format(number // 10, number % 10), end=", ")
else:
    print("99")
