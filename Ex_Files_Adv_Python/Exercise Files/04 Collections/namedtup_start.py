# Demonstrate the usage of namdtuple objects

import collections


def main():
    # TODO: create a Point namedtuple
    p = collections.namedtuple("point", 'x y')

    p1 = p(10, 20)
    print(p1)
    # TODO: use _replace to create a new instance
    # tuples are immutable
    print(p1._replace(x=100))


if __name__ == "__main__":
    main()
