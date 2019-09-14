def safe_pawns(pawns: set) -> int:
    pawan_indexs = set()

    for pawn in pawns:
        row = int(pawn[1]) - 1
        col = ord(pawn[0]) - 97
        pawan_indexs.add((row, col))

    count = 0

    for row, col in pawan_indexs:
        is_safe = ((row - 1, col - 1) in pawan_indexs) or ((row - 1, col + 1) in pawan_indexs)
        if is_safe:
            count += 1

    return count


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")