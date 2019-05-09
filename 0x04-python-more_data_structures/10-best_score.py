#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None:
        keys, values = list(a_dictionary.keys()), list(a_dictionary.values())
        return keys[values.index(max(values))]
    else:
        return None
