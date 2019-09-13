def collection_conversions():
    list_one = [10, 25, 35, 40, 40, 35, 25, 55, 66, 88]
    set_one = {100, 255, 355, 440, 654, 878}
    dic_one = {'name': 'Pavan Kumar', 'city': 'Hyderabad'}
    list_two = list([45, 88, 65, 45, 105, 205, 205])
    set_two = set({44, 55, 66, 77, 88, 99, 44, 55})
    dic_two = dict({'name': 'Sai', 'city': 'Ongole'})
    tup = ('val', 10, 25, 65, 888, 789, 456)
    print(list_one)
    print(list_two)
    print(set_one)
    print(set_two)
    print(dic_one)
    print(dic_two)
    print(set(list_one))
    print(list(set_one))
    print(set(tup))
    dic_three = dict(iterable=set_one)
    print(dic_three.keys())
    print(dic_three['iterable'].__class__)
    print(dic_three.values())


a = 10


class _CustomeClass:
    b = 10
    _c = 20
    __d = 30

    def add(self, num1, num2):
        return num1+num2

    def _multiple(self, num1, num2):
        return num1*num2

    def __power_(self, num1, num2):
        return num1 ** num2


if __name__ == '__main__':
    obj = _CustomeClass()
    print(obj.b)
    print(obj.__power_(5, 5))
    collection_conversions()
