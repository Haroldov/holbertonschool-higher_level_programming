#!/usr/bin/python3
def number_of_lines(filename=""):
    with open(filename) as f:
        return sum([1 for line in f])
