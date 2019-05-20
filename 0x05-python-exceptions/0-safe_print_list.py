#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        i = -1
        for i in range(x):
            print(my_list[i], end="")
    except:
        if i > 0:
            i -= 1
        else:
            i = -1
    finally:
        print()
        return i + 1
