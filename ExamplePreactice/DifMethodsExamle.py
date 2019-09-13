class ClassOne:
    message = 'Hello World !!!'

    def __init__(self):
        self.z = 100;

    def add(obj, a, b):
        print('In Add method: ', obj.z)
        obj.z = 1000;
        print('In Add method: ', obj.z)
        obj.message = 56
        return a+b+obj.message

    def sum(self, c, d):
        print(self.z)
        return c+d

    @classmethod
    def show(pkn):
        # print(pkn.z)
        pkn.add(ClassOne(), 10, 30)
        return pkn.message + "It is Class method"

    @staticmethod
    def mul(a, b):
        return a*b


if __name__ == '__main__':
    print(ClassOne.add(ClassOne(), 100, 20))
    print(ClassOne.show())
    print(ClassOne.mul(10, 5))
    print(ClassOne.sum(ClassOne(), 10, 20))
