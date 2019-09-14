from typing import List


def checkio(game_result: List[str]) -> str:
    # checkio = lambda g: max((__import__('re')).match(r'(?:(?:...)*(X|O)\1\1)|(?:.*(X|O)(?:..\2..\2))|(?:(X|O)(?:...\3...\3))|(?:..(X|O)(?:.\4.\4))|()', ''.join(g)).groups() + ('D',), key=bool)
    # s1, s2, s3 = g
    # s4 = tuple(g[0][0] + g[1][1] + g[2][2])
    # s5 = tuple(g[0][2] + g[1][1] + g[2][0])
    # a = list(zip(s1, s2, s3))
    # a.extend([s4, s5, tuple(g[0]), tuple(g[1]), tuple(g[2])])
    # for x in range(len(a)):
    #     if len(set(a[x])) == 1:
    #         if a[x][0] in 'XO':
    #             return a[x][0]
    #     else: continue
    # return 'D'

    
    if game_result[0][0] == game_result[1][1] == game_result[2][2] and game_result[0][0] != '.':
        return game_result[0][0]
    elif game_result[2][0] == game_result[1][1] == game_result[0][2] and game_result[0][2] != '.':
        return game_result[2][0]

    for row in game_result:
        if row[0] == row[1] == row[2] and row[0] != '.':
            return row[0]

    rotate_field = list(zip(*game_result))
    for field in rotate_field:
        if field[0] == field[1] == field[2] and field[0] != '.':
            return field[0]

    return "D"


if __name__ == '__main__':
    print("Example:")
    print(checkio(["X.O",
                   "XX.",
                   "XOO"]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
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
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")