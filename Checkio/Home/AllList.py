from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:
    # your code here
    print(True if len(elements) == 0 else elements.count(elements[0]) == len(elements))
    # print(len(elements))
    if len(elements) == 0 or len(elements) == 1:
        return True
    else:
        for idx in range(len(elements)):
            if idx+1 == len(elements):
                return True
            elif elements[idx] != elements[idx+1]:
                return False


if __name__ == '__main__':
    print("Example:")
    # print(all_the_same([1, 1, 1]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert all_the_same([1, 1, 1]) == True
    assert all_the_same([1, 2, 1]) == False
    assert all_the_same(['a', 'a', 'a']) == True
    assert all_the_same([]) == True
    assert all_the_same([1]) == True
    print("Coding complete? Click 'Check' to earn cool rewards!")