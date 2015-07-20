def find_message(text):
    secret_message = ""
    for word in text:
        for ch in word:
            if ch.isupper() is True:
                secret_message = secret_message + ch
    return secret_message

if __name__ == '__main__':

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO", "hello"
    assert find_message("hello world!") == "", "Nothing"
    assert find_message("HELLO WORLD!!!") == "HELLOWORLD", "Capitals"
