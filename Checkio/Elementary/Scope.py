from Checkio.Elementary import CollectionExample


class MyClass:
    __name = 'Pavan'
    age = 23
    __city = 'Ongole'

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str):
        self.__name = name


class MyClass1:
    __city = 'Hyderabad'

    def getName(self, myclass: MyClass):
        print(myclass.get_name())


def main():
    print("In Main")
    obj = MyClass()
    obj1 = MyClass()
    obj2 = MyClass()
    obj3 = MyClass1()
    print(obj.get_name())
    obj.set_name('Ram')
    obj1.set_name('krishna')
    print(obj.get_name())
    print(obj1.get_name())
    print(obj2.get_name())
    obj1.age = 18
    print(obj1.age)
    print(obj.age)
    obj3.getName(obj)
    print(CollectionExample.collection_conversions())
    print(CollectionExample.a)
    print(CollectionExample.__CustomeClass._c)
    print(CollectionExample.__CustomeClass.add(CollectionExample.__CustomeClass(), 20, 10))
    print(CollectionExample.__CustomeClass._multiple(CollectionExample.__CustomeClass(), 20, 10))
    # print(CollectionExample.__CustomeClass.__power(CollectionExample.__CustomeClass(), 20, 10))
    # print(CollectionExample.__CustomeClass.__d)

if __name__ == '__main__':
    main()
