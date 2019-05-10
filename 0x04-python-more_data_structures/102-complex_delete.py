#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for keys, vals in a_dictionary.copy().items():
        if value in vals:
            del a_dictionary[keys]
    return a_dictionary
