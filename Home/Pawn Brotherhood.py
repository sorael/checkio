def safe_pawns(pawns):
    pawn = 0
    for i in pawns:
        col, row = list(i)
        if row == 1:
            continue
        if 'a' not in col:
            if chr(ord(col) - 1) + str(int(row) - 1) in pawns:
                pawn += 1
                continue
        if 'h' not in col:
            if chr(ord(col) + 1) + str(int(row) - 1) in pawns:
                pawn += 1
    return pawn

if __name__ == '__main__':

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6, "1nd example"
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1, "2nd example"
