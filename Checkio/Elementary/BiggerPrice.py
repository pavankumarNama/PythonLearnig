def bigger_price(limit: int, data: list) -> list:
    """
        TOP most expensive goods
    """
    # your code here
    # l = sorted([d['price'] for d in data], reverse=True)
    # result = []
    # for i in l[0:limit]:
    #     m = list(k for k in data if k['price'] == i)
    #     result.append(m[0])
    # return result
    return sorted(data, key=lambda k: k['price'], reverse=True)[0:limit]


if __name__ == '__main__':
    from pprint import pprint
    print('Example:')
    pprint(bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]))

    # These "asserts" using for self-checking and not for auto-testing
    assert bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]) == [
               {"name": "wine", "price": 138},
               {"name": "bread", "price": 100}
           ], "First"

    assert bigger_price(1, [
        {"name": "pen", "price": 5},
        {"name": "whiteboard", "price": 170}
    ]) == [{"name": "whiteboard", "price": 170}], "Second"

    print('Done! Looks like it is fine. Go and check it')
