# Demonstrate the use of keyword-only arguments


# use keyword-only arguments to help ensure code clarity
def myFunction(a, b, *, arg=False):
    print(a, b, arg)


def main():
    # try to call the function without the keyword
    # myFunction(1, 2, True)
    myFunction("1", '2', arg=True)


if __name__ == "__main__":
    main()
