#!/usr/bin/python3
def no_c(my_string):
    new_str = [c for c in my_string if c != "c" and c != "C"]
    new_str = "".join(new_str)
    return(new_str)
