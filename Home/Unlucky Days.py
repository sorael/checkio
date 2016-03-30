from datetime import date, timedelta


def first_friday(year):
    d = date(year, 1, 1)
    first_day = d.isoweekday()
    if first_day == 1:
        return d + timedelta(days=4)
    elif first_day == 2:
        return d + timedelta(days=3)
    elif first_day == 3:
        return d + timedelta(days=2)
    elif first_day == 4:
        return d + timedelta(days=1)
    elif first_day == 5:
        return d
    elif first_day == 6:
        return d + timedelta(days=6)
    else:
        return date(year, 1, 1) + timedelta(days=5)


def checkio(year):
    f_friday = first_friday(year)
    count = 0
    for i in range(0, 366, 7):
        f = f_friday + timedelta(days=i)
        ass = str(f).split('-')
        if ass[2] == "13" and ass[0] == str(year):
            count += 1
    return count


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    assert checkio(2015) == 3, "First - 2015"
    assert checkio(1986) == 1, "Second - 1986"
