class A:
    def add(self, a: int, b: int):
        print('In ClassA: ', a+b)


class B(A):
    print()


class C(B):
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b
        B.add(self, a, b)


if __name__ == '__main__':
    c = C('P', 'K')
    print(C.mro().__class__)
    print(C.__mro__.__class__)

