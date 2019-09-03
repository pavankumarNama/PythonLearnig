# Demonstrate the use of function docstrings


def myFunction(arg1, arg2=None):
    """Example for method documentation

    :param arg1:
    :param arg2:
    """
    print(arg1, arg2)


def main():
    print(myFunction.__doc__)


if __name__ == "__main__":
    main()
