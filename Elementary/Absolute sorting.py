def checkio(numbers_array):
    number_list = list(numbers_array)
    n = 1
    while n < len(number_list):
        for i in range(len(number_list)-n):
            if abs(number_list[i]) > abs(number_list[i+1]):
                number_list[i],number_list[i+1] = number_list[i+1],number_list[i]
        n += 1
    return number_list

if __name__ == '__main__':
    def check_it(array):
        if not isinstance(array, (list, tuple)):
            raise TypeError("The result should be a list or tuple.")
        return list(array)

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_it(checkio((-20, -5, 10, 15))) == [-5, 10, 15, -20], "Example"  # or (-5, 10, 15, -20)
    assert check_it(checkio((1, 2, 3, 0))) == [0, 1, 2, 3], "Positive numbers"
    assert check_it(checkio((-1, -2, -3, 0))) == [0, -1, -2, -3], "Negative numbers"
