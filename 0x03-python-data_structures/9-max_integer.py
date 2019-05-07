#!/usr/bin/python3
def max_integer(my_list=[]):
    num_max = 0
    if len(my_list) == 0:
        return None
    else:
        for num in my_list:
            if num > num_max:
                num_max = num
        return num_max
