#!/usr/bin/python3
def uppercase(str):
    length = len(str)
    if length == 0:
        return
    cad = ""
    for ind, char in enumerate(str):
        if ind == length - 1:
            cad = "\n"
        ascii = ord(char)
        if ascii >= 97 and ascii <= 122:
            ascii -= 32
        print("{}".format(chr(ascii)), end=cad)
    return
