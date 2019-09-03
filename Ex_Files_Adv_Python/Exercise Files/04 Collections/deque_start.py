# deque objects are like double-ended queues

import collections
import string


def main():

    # TODO: initialize a deque with lowercase letters
    alpha = collections.deque(string.ascii_lowercase)
    # TODO: deques support the len() function
    print(len(alpha))
    # TODO: deques can be iterated over
    for a in alpha:
        print(a.upper(), end=',')
    # TODO: manipulate items from either end
    print()
    print(alpha.pop())
    print(alpha.popleft())
    alpha.append(2)
    alpha.appendleft(1)
    print(alpha)
    # TODO: rotate the deque
    print(alpha)
    alpha.rotate(-1)
    print(alpha)


if __name__ == "__main__":
    main()
