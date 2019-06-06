#!/usr/bin/python3


def pascal_triangle(n):
    if n <= 0:
        return []
    triag = [[1]]
    for i in range(n - 1):
        row = [1]
        if len(triag[i]) == 1:
            row += [1]
        else:
            row += [x + y for x, y in zip(triag[i], [0] + triag[i][:-1])][1:]
            row += [1]
        triag.append(row)
    return triag
