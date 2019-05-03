#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argc = len(argv)
    char = ":"
    if argc == 1:
        char = "."
    elif argc == 2:
        str = "argument"
    else:
        str = "arguments"
    print("{0:d} {2:s}{1:s}".format(argc - 1, char, str))
    for i, arg in enumerate(argv[1::], start=1):
        print("{0:d}: {1:s}".format(i, arg))
