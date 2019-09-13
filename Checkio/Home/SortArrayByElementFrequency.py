from collections import Counter


def frequency_sort(items):
    # your code here

    # Simple sort method in list
    # print(sorted(items, key=items.count, reverse=True))

    items = sorted(items, key=lambda i: items.index(i))
    # sorted(items, key=lambda x : items.count(x), reverse=True)
    print(items)

    # d = Counter(items)
    # s = sorted(d, key=d.get, reverse=True)
    # print([[k]*v for k, v in Counter(items).items()])
    return sum([[k]*v for k, v in Counter(items).items()], [])
    # sum([[k]*d[k] for k in s], [])


if __name__ == '__main__':
    print("Example:")
    # print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")
