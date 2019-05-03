#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argc = len(argv)
    char = ":"
    if argc == 1:
        char = "."
    print("{0:d} arguments{1:s}".format(argc - 1, char))
    for i, arg in enumerate(argv[1::], start=1):
        print("{0:d}: {1:s}".format(i, arg))
