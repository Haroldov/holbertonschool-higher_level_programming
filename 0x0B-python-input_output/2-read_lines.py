#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    with open(filename) as f:
        if nb_lines == 0 or nb_lines >= sum([1 for line in f]):
            print(f.read(), end='')
        else:
            f.seek(0)
            for numLine, line in enumerate(f):
                print(line, end='')
                if numLine + 1 == nb_lines:
                    break
            
