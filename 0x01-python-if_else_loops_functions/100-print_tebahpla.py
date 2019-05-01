#!/usr/bin/python3
for i in range(25, -1, -1):
    if (i % 2 == 0):
        i -= 32
    print("{}".format(chr(i + 97)), end="")
