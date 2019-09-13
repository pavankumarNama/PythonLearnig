def best_stock(data):
    # your code here
    temp = 0.0
    # print(max(data, key=data.__getitem__))
    print(max(data, key=lambda d: data[d]))
    key = None
    for k in data:
        if temp < data[k]:
            temp = data[k]
            key = k
    return key


if __name__ == '__main__':
    print("Example:")
    print(best_stock({
        'CAC': 10.0,
        'ATX': 390.2,
        'WIG': 1.2
    }))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert best_stock({
        'CAC': 10.0,
        'ATX': 390.2,
        'WIG': 1.2
    }) == 'ATX', "First"
    assert best_stock({
        'CAC': 91.1,
        'ATX': 1.01,
        'TASI': 120.9
    }) == 'TASI', "Second"
    print("Coding complete? Click 'Check' to earn cool rewards!")