def su(data, i, total):
    if i >= len(data):
        return total
    return su(data, i + 1, total + data[i])


def checkio(data):
    return su(data, 0, 0)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([1, 2, 3]) == 6
    assert checkio([2, 2, 2, 2, 2, 2]) == 12
