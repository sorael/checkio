def longest_palindromic(text):
    palindrome = ''
    for i in range(len(text)):
        for j in range(i, len(text)+1):
            if len(text[i:j]) > len(palindrome):
                if text[i:j] == text[i:j][::-1]:
                    palindrome = text[i:j]
    return palindrome


if __name__ == '__main__':
    assert longest_palindromic("artrartrt") == "rtrartr", "The Longest"
    assert longest_palindromic("abacada") == "aba", "The First"
    assert longest_palindromic("aaaa") == "aaaa", "The A"
    assert longest_palindromic(" ddd aaaa ") == " aaaa ", "The A"
