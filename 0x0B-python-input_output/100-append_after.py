#!/usr/bin/python3


def append_after(filename="", search_string="", new_string=""):
    with open(filename, 'a+') as f:
        for line in f:
            if search_string in line:
                f.write(new_string)
