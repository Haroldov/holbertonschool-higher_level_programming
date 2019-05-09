#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    key, val = list(a_dictionary.keys()), list(a_dictionary.values())
    val_2 = list(map(lambda x: 2 * x, val))
    return dict(zip(key, val_2))
