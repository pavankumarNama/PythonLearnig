from collections import Counter


def second_index(text: str, symbol: str) -> [int, None]:
    """
        returns the second index of a symbol in a given text
    """
    # your code here
    # Short answer
    return text.index(symbol, text.index(symbol)+1) if text.count(symbol) >= 2 else None

    # count = 0
    # index = 0
    # i = None
    # for t in text:
    #     if t == symbol:
    #         count += 1
    #     if count == 2:
    #         i = index
    #         return i
    #     index += 1
    # return i


if __name__ == '__main__':
    print('Example:')
    # print(second_index("sims", "s"))
    print(second_index("find the river", "e"))
    # These "asserts" are used for self-checking and not for an auto-testing
    assert second_index("sims", "s") == 3, "First"
    assert second_index("find the river", "e") == 12, "Second"
    assert second_index("hi", " ") is None, "Third"
    assert second_index("hi mayor", " ") is None, "Fourth"
    assert second_index("hi mr Mayor", " ") == 5, "Fifth"
    print('You are awesome! All tests are done! Go Check it!')
