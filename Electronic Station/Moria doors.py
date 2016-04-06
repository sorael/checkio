def calc_similarity(word1, word2):
    word1_len = len(word1)
    word2_len = len(word2)
    unique_letters_numbers = len(set(word1 + word2))
    common_letter_number = len(set(word1) & set(word2))

    similarity = 10 * (word1[0] == word2[0])
    similarity += 10 * (word1[-1] == word2[-1])
    if word1_len <= word2_len:
        similarity += (word1_len / word2_len) * 30
    else:
        similarity += (word2_len / word1_len) * 30
    similarity += (common_letter_number / unique_letters_numbers) * 50
    return similarity


def find_word(message):
    words = message.replace('.', '').replace(',', '').lower().split()
    summary = [[0, word] for word in words]
    for i, I in enumerate(words):
        for j, J in enumerate(words):
            if i != j:
                summary[i][0] += calc_similarity(I, J)
    return max(summary)[1]

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_word("Friend Fred and friend Ted.") == "friend", "Friend"
    assert find_word("Speak friend and enter.") == "friend", "Friend"
    assert find_word("Beard and Bread") == "bread", "Bread is Beard"
    assert find_word("The Doors of Durin, Lord of Moria. Speak friend and enter. "
                     "I Narvi made them. Celebrimbor of Hollin drew these signs") == "durin", "Durin"
    assert find_word("Aoccdrnig to a rscheearch at Cmabrigde Uinervtisy."
                     " According to a researcher at Cambridge University.") == "according", "Research"
    assert find_word("One, two, two, three, three, three.") == "three", "Repeating"
