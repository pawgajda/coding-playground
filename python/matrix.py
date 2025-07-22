#!/usr/bin/env python3


def multiply(a, b):
    # initialize empty result table
    result = []

    # rows(a) * columns(b) when columns(a) == rows(b)
    if len(a) >= 0 and len(a[0]) == len(b):
        # i - row of a
        for i in range(0, len(a)):
            # initialize empty row result[[]]
            result.append([])
            # j - column of b
            for j in range(0, len(b[0])):
                # initialize empty column result[[0]]
                result[i].append(0)
                # k = common (rows of a, columns of b)
                for k in range(0, len(b)):
                    # a[i][k] * b[k][j]
                    result[i][j] += a[i][k] * b[k][j]

    return result


def add(a, b):
    result = []

    if len(a) >= 0 and len(b) >= 0:
        if len(a) == len(b) and len(a[0]) == len(b[0]):
            # iterate through rows
            for i in range(0, len(a)):
                # create empty row in result matrix
                result.append([])
                # iterate through columns
                for j in range(0, len(a[0])):
                    # append column to row
                    result[i].append(a[i][j] + b[i][j])

    return result


def transposition(a):
    result = []
    if len(a) >= 0 and len(a[0]) >= 0:
        # columns of a
        for i in range(0, len(a[0])):
            # create empty row in result matrix
            result.append([])
            # rows of a
            for j in range(0, len(a)):
                # append value of column to row
                result[i].append(a[j][i])

    return result

if __name__ == "__main__":
    # rows: len(a) == 3
    # columns: len(a[0]) == 2
    # x = [1, 0]
    a = [
        [1, 0],
        [2, -1],
        [1, 2],
    ]

    # rows: len(b) == 2
    # columns: len(b[0]) == 4
    b = [
        [2, -2, 0, 2],
        [1, 3, -1, 1],
    ]

    result = multiply(a, b)
    print(result)

    result_transposition = transposition(result)
    print(result_transposition)

    result = multiply(result_transposition, a)
    print(result)

    c = [
        [3, 8],
        [4, 6],
    ]

    d = [
        [4, 0],
        [1, -9],
    ]

    addition_result = add(c, d)
    print(addition_result)

    e = [
        [60512, 31232, 2137, 9999],
        [15515, 11111, 55555, 1],
        [28, 6912, 10800, 21800],
        [7945, 14975, 420, 21711],
    ]
