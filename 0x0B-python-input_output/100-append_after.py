#!/usr/bin/python3


def append_after(filename="", search_string="", new_string=""):
    offset = 0
    with open(filename, 'r') as f:
        for line in f:
            offset += len(line)
            if search_string in line:
                with open(filename, 'r') as af:
                    first_half = af.read(offset)
                    af.seek(offset, 0)
                    second_half = af.read()
                with open(filename, 'w') as af:
                    af.write(first_half)
                with open(filename, 'a') as af:
                    af.write(new_string + second_half)
                offset += len(new_string)
