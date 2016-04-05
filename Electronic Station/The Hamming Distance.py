def checkio(n, m):
    n_str = str(bin(n))[2:]
    m_str = str(bin(m))[2:]
    n_len = len(n_str)
    m_len = len(m_str)

    if n_len != m_len:
        if n_len > m_len:
            m_str = m_str.rjust(n_len, '0')
        else:
            n_str = n_str.rjust(m_len, '0')

    distance = 0
    for x, y in zip(n_str, m_str):
        if x != y:
            distance += 1

    return distance


def checkio2(n, m):
    return bin(n ^ m).count('1')



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(117, 17) == 3, "First example"
    assert checkio(1, 2) == 2, "Second example"
    assert checkio(16, 15) == 5, "Third example"

    assert checkio2(117, 17) == 3, "First example"
    assert checkio2(1, 2) == 2, "Second example"
    assert checkio2(16, 15) == 5, "Third example"
