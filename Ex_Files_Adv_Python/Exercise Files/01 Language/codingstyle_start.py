class Person:
    __name = "Nama"

    # python has access modifiers public, protected and private.
    # single '_'before variable name shows it's protected
    # double '__'before variable name shows it's private. if doesn't
    # have ani '_' symbols it is public.
    # have ani '_' symbols it is public.

    def __init__(self, name):
        self.__name = name
        # 'self' keyword is works like 'this' keyword in java
        print("Person name is : ", name)

    def ageofperson(self, age):
        if age < 0:
            print('Age can"t be negative')
            return


if __name__ == "__main__":
    p1 = Person("Pavan")
    p1.ageofperson(-40)
    print(p1.ageofperson)
