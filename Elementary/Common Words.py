def checkio(first, second):
    return ','.join(sorted(set(first.split(',')) & set(second.split(','))))

if __name__ == '__main__':

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("hello,world", "hello,earth") == "hello", "Hello"
    assert checkio("one,two,three", "four,five,six") == "", "Too different"
    assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two", "1 2 3"
