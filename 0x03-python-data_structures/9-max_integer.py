#!/usr/bin/python3
def max_integer(my_list=[]):
    num_max = []
    if len(my_list) == 0:
        return None
    else:
        for num in my_list:
            if len(num_max) == 0:
                num_max.append(num)
            else:
                if num > num_max[0]:
                    num_max[0] = num
        return num_max[0]
