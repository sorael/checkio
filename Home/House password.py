def checkio(data):
    digit = 0
    lower = 0
    upper = 0
    if len(data) < 10:
        return False
    for i in data:
        if i.isdigit():
            digit += 1
        if i.islower():
            lower += 1
        if i.isupper():
            upper += 1
    if digit > 0 and lower > 0 and upper > 0:
        return True
    else:
        return False

if __name__ == '__main__':

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') is False, "1st example"
    assert checkio('bAse730onE4') is True, "2nd example"
    assert checkio('asasasasasasasaas') is False, "3rd example"
    assert checkio('QWERTYqwerty') is False, "4th example"
    assert checkio('123456123456') is False, "5th example"
    assert checkio('QwErTy911poqqqq') is True, "6th example"
