# advanced iteration functions in the itertools package
import itertools


def testFunction(x):
    return x < 40


def main():
    # TODO: cycle iterator can be used to cycle over a collection
    seq1 = ["Joe", "John", "Mike"]
    # c = itertools.cycle(seq1)
    # print(next(c))
    # print(next(c))
    # print(next(c))
    # print(next(c))
    # TODO: use count to create a simple counter
    # c = itertools.count(100, 10)
    # print(next(c))
    # print(next(c))
    # print(next(c))
    # print(next(c))
    # TODO: accumulate creates an iterator that accumulates values
    vals = [10,20,30,40,50,40,30]
    # a = itertools.accumulate(vals)
    # print(next(a))
    # print(next(a))
    # print(next(a))
    # print(next(a))
    # print(next(a))
    # print(next(a))
    # print(next(a))

    # TODO: use chain to connect sequences together
    # i = list(itertools.chain("PAVAN", "Python"))
    # print(i)
    # TODO: dropwhile and takewhile will return values until
    # a certain condition is met that stops them
    dw = list(itertools.dropwhile(testFunction, vals))
    tw = list(itertools.takewhile(testFunction, vals))
    print(dw)
    print(tw)


if __name__ == "__main__":
    main()
