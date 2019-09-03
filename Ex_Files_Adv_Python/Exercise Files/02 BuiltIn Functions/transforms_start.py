# use transform functions like sorted, filter, map


def filterFunc(x):
    if (x % 2) == 0:
        return False
    return True


def filterFunc2(x):
    if str(x).isupper():
        return True
    return False


def squareFunc(x):
    return x*x


def toGrade(x):
    if x > 90 :
        return 'A'
    elif (x > 80 and x <= 90):
        return 'B'
    else:
        return 'C'


def main():
    # define some sample sequences to operate on
    nums = (1, 8, 4, 5, 13, 26, 381, 410, 58, 47)
    chars = "abcDeFGHiJklmnoP"
    grades = (81, 89, 94, 78, 61, 66, 99, 74)

    # TODO: use filter to remove items from a list
    i = list(filter(filterFunc, nums))
    print(i)
    # TODO: use filter on non-numeric sequence
    c = list(filter(filterFunc2, chars))
    print(c)
    # TODO: use map to create a new sequence of values
    s = list(map(squareFunc, nums))
    print(s)
    # TODO: use sorted and map to change numbers to grades
    grades = sorted(grades)
    print(grades)
    g = list(map(toGrade, grades))
    print(g)


if __name__ == "__main__":
    main()
