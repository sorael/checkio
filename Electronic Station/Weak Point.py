def weak_point(matrix):
    rows = []
    for i in matrix:
        rows.append(sum(i))
    row = min((row_sum, index) for (index, row_sum) in enumerate(rows))
    columns = zip(*matrix[::-1])
    cols = []
    for i in columns:
        cols.append(sum(i))
    col = min((col_sum, index) for (index, col_sum) in enumerate(cols))
    return [row[1], col[1]]


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    assert isinstance(weak_point([[1]]), (list, tuple)), "The result should be a list or a tuple"
    assert list(weak_point([[7, 2, 7, 2, 8],
                            [2, 9, 4, 1, 7],
                            [3, 8, 6, 2, 4],
                            [2, 5, 2, 9, 1],
                            [6, 6, 5, 4, 5]])) == [3, 3], "Example"
    assert list(weak_point([[7, 2, 4, 2, 8],
                            [2, 8, 1, 1, 7],
                            [3, 8, 6, 2, 4],
                            [2, 5, 2, 9, 1],
                            [6, 6, 5, 4, 5]])) == [1, 2], "Two weak point"
    assert list(weak_point([[1, 1, 1],
                            [1, 1, 1],
                            [1, 1, 1]])) == [0, 0], "Top left"
