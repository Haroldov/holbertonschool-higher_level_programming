#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    tmp = 0
    pastNum = 0
    for c in roman_string:
        tmp = dic.get(c, 0)
        if tmp > pastNum:
            num -= 2 * pastNum
            num += tmp
        else:
            num += tmp
        pastNum = tmp
    return num
