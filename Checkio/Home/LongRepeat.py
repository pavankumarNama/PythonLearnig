from collections import Counter

import numpy
import re


def long_repeat(line: str) -> int:
    """
        length the longest substring that consists of the same char
    """
    pattern = r"(.)\1*"
    print(max([0]+[len(m.group()) for m in re.finditer(pattern, line)]))
    return max([0]+[len(m.group()) for m in re.finditer(pattern, line)])

    # if len(line) == 0:
    #     return 0
    # elif len(line) == 1:
    #     return 1
    # else:
    #     count = 1
    #     count_list = []
    #     for i in range(len(line)-1):
    #         if line[i] == line[i+1]:
    #             count += 1
    #         else:
    #             count = 1
    #         count_list.append(count)
    #
    #     return max(count_list)



if __name__ == '__main__':
    #T hese "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    assert long_repeat("a") == 1
    print('"Run" is good. How is "Check"?')