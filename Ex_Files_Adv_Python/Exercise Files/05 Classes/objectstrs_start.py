# customize string representations of objects


class Person():
    def __init__(self):
        self.fname = "Joe"
        self.lname = "Marini"
        self.age = 25

    # TODO: use __repr__ to create a string useful for debugging
    def __repr__(self):
        return "First Name " + self.fname + " Last Name " + self.lname + " Age " + str(self.age)

    # TODO: use str for a more human-readable string
    def __str__(self):
        return "FName :: " + self.fname + " LName :: " + self.lname + " Age of person is :: " + str(self.age)


def main():
    # create a new Person object
    cls1 = Person()

    # use different Python functions to convert it to a string
    print(repr(cls1))
    print(str(cls1))
    print("Formatted: {0}".format(cls1))


if __name__ == "__main__":
    main()
