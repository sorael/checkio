import re

VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"


def checkio(text):
    text = text.upper()
    tokens = re.split("[^A-Z0-9]+", text)
    count = 0
    for i in tokens:
        if len(i) <= 1 or not i.isalpha():
            continue
        is_valid = True
        for j in range(0, len(i)-1):
            if VOWELS.find(i[j]) != -1 and VOWELS.find(i[j+1]) != -1:
                is_valid = False
                break
            if CONSONANTS.find(i[j]) != -1 and CONSONANTS.find(i[j+1]) != -1:
                is_valid = False
                break
        if is_valid:
            count += 1
    return count

if __name__ == '__main__':

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("My name is ...") == 3, "All words are striped"
    assert checkio("Hello world") == 0, "No one"
    assert checkio("A quantity of striped words.") == 1, "Only of"
    assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
