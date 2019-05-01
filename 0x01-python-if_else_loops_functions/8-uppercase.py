#!/usr/bin/python3
def uppercase(str):
    for ind, char in enumerate(str):
        ascii = ord(char)
        if ascii >= 97 and ascii <= 122:
            ascii -= 32
        print("{}".format(chr(ascii)), end="")
    else:
        print()
