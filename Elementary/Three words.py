def checkio(words):
    my_list = words.split(" ")
    check = 0
    for i in my_list:
        if i.isalpha() is True:
            check += 1
            if check == 3:
                return True
        else:
            check = 0
    if check >= 3:
        return True
    else:
        return False

if __name__ == '__main__':

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World hello") is True, "Hello"
    assert checkio("He is 123 man") is False, "123 man"
    assert checkio("1 2 3 4") is False, "Digits"
    assert checkio("bla bla bla bla") is True, "Bla Bla"
    assert checkio("Hi") is False, "Hi"
