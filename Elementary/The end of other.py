def checkio(words_set):
    if len(words_set) == 1:
        return False
    for suffix in words_set:
        for word in words_set - {suffix}:
            if word.endswith(suffix):
                return True
    return False

if __name__ == '__main__':

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio({"hello", "lo", "he"}) is True, "helLO"
    assert checkio({"hello", "la", "hellow", "cow"}) is False, "hellow la cow"
    assert checkio({"walk", "duckwalk"}) is True, "duck to walk"
    assert checkio({"one"}) is False, "Only One"
    assert checkio({"helicopter", "li", "he"}) is False, "Only end"
