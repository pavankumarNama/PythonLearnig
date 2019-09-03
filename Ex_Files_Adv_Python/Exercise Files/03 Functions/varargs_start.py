# Demonstrate the use of variable argument lists


# TODO: define a function that takes variable arguments
def addition(base, base2: str, numbers: list):
    print("Base:: ", base)
    print("Base:: ", base2 + base)
    print("class:: ", numbers.__class__)
    result = 0
    for number in numbers:
        result = result + number
    return result


def main():
    # TODO: pass different arguments
    # print(addition(1, 2, 3, 4, 5, 6))
    # print(addition(10, 20, 30, 40, 50, 60))
    # print(addition(12, 23, 34, 45, 56, 67))

    # TODO: pass an existing list
    a = [12, 23, 34, 45, 56, 67]
    print(addition(1, 2, (1, 2, 3)))


if __name__ == "__main__":
    main()
