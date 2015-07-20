def checkio(number):
    number_2_string = str(number)
    total = 1
    for i in number_2_string:
        if int(i) > 0:
            total *= int(i)
    return total

if __name__ == '__main__':

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
