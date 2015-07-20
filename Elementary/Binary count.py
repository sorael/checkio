def checkio(number):
    return bin(number).count("1")

if __name__ == '__main__':

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 1
    assert checkio(15) == 4
    assert checkio(1) == 1
    assert checkio(1022) == 9
