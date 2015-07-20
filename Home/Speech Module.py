FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):
    result = []
    hundred = (number // 100)
    if hundred > 0:
        result.append(FIRST_TEN[hundred - 1])
        result.append(HUNDRED)

    second_ten = number % 100
    if (second_ten >= 10) and second_ten <= 19:
        result.append(SECOND_TEN[second_ten - 10])
        return " ".join(result)

    other_tens = second_ten // 10
    if other_tens > 1:
        result.append(OTHER_TENS[other_tens - 2])

    units = second_ten % 10
    if units > 0:
        result.append(FIRST_TEN[units - 1])

    return " ".join(result)

if __name__ == '__main__':

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
