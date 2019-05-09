#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list or my_list is None:
        return 0
    acum = 0
    denom = 0
    for num, mul in my_list:
        acum += num * mul
        denom += mul
    return acum / denom
