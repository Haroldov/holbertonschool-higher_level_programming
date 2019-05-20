#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):
            print(my_list[i], end="")
    except:
        i -= 1
        pass
    finally:
        print()
        return i + 1
