#!/usr/bin/python3
def uppercase(str):
    length = len(str)
    cad = ""
    for ind, char in enumerate(str):
        if ind == length - 1:
            cad = "\n"
        ascii = ord(char)
        if ascii >= 97 and ascii <= 122:
            print("{}".format(chr(ascii - 32)), end=cad)
        else:
            print("{}".format(chr(ascii)), end=cad)
    return
