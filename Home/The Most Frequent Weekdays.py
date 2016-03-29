from datetime import date


def most_frequent_days(year):
    """
    List of most frequent days of the week in the given year
    """
    months = ['1Monday', '2Tuesday', '3Wednesday', '4Thursday',
              '5Friday', '6Saturday', '7Sunday']

    def days(d, w):
        if w == 0:
            return months[d-1:]
        elif w == 1:
            return months[:d]

    def create_sort_list(d):
        days_list = [i for i in d]
        days_list.sort()
        return [i[1:] for i in days_list]

    first_weak = days(date(year, 1, 1).isoweekday(), w=0)
    last_weak = days(date(year, 12, 31).isoweekday(), w=1)

    _days = {}
    for i in first_weak + last_weak:
        if i not in _days:
            _days[i] = 1
        else:
            _days[i] += 1

    if set(_days.values()) == {1}:
        return create_sort_list(_days)

    for j in list(_days):
        if _days[j] == 1:
            _days.pop(j)

    return create_sort_list(_days)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert most_frequent_days(328) == ["Monday","Sunday"], "0st example"
    assert most_frequent_days(2399) == ['Friday'], "1st example"
    assert most_frequent_days(1152) == ['Tuesday', 'Wednesday'], "2nd example"
    assert most_frequent_days(56) == ['Saturday', 'Sunday'], "3rd example"
    assert most_frequent_days(2909) == ['Tuesday'], "4th example"
