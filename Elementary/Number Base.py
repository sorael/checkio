def checkio(str_number, radix):
    try:
        return int(str_number, radix)
    except ValueError:
        return -1

if __name__ == '__main__':

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("AF", 16) == 175, "Hex"
    assert checkio("101", 2) == 5, "Bin"
    assert checkio("101", 5) == 26, "5 base"
    assert checkio("Z", 36) == 35, "Z base"
    assert checkio("AB", 10) == -1, "B > A > 10"
