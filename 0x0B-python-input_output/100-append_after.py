#!/usr/bin/python3


def append_after(filename="", search_string="", new_string=""):
    with open(filename, 'r') as f:
        text = f.read()
    lines = text.split('\n')
    try:
        lines.remove('')
    except:
        pass
    count = 1
    for numLine, line in enumerate(lines[:]):
        if search_string in line:
            lines = (lines[:numLine + count] +
                     [new_string.replace('\n', '')] + lines[numLine + count:])
            count += 1
    new_text = "\n".join(lines) + '\n'
    with open(filename, 'w') as f:
        f.write(new_text)
