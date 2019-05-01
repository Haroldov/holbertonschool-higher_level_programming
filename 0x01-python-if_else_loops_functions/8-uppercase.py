#!/usr/bin/python3
def uppercase(str):
    upStr = ""
    for char in str:
        ascii = ord(char)
        if ascii >= 97 and ascii <= 122:
            upStr += chr(ascii - 32)
        else:
            upStr += chr(ascii)
    else:
        print(upStr)
