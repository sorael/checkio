def checkio(game_result):
    i = 0
    while i < 3:
        line = game_result[i]
        if line == "XXX":
            return "X"
        if line == "OOO":
            return "O"
        i += 1

    j = 0
    while j < 3:
        column = game_result[0][j] + game_result[1][j] + game_result[2][j]
        if column == "XXX":
            return "X"
        if column == "OOO":
            return "O"
        j += 1

    d1 = game_result[0][0] + game_result[1][1] + game_result[2][2]
    d2 = game_result[2][0] + game_result[1][1] + game_result[0][2]
    diagonals = [d1, d2]
    k = 0
    while k < 2:
        diagonal = diagonals[k]
        if diagonal == "XXX":
            return "X"
        if diagonal == "OOO":
            return "O"
        k += 1
    return "D"

if __name__ == '__main__':

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
