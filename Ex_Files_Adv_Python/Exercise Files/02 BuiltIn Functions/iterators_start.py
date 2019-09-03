# use iterator functions like enumerate, zip, iter, next


def main():
    # define a list of days in English and French
    days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    daysFr = ["Dim", "Lun", "Mar", "Mer", "Jeu", "Ven", "Sam"]

    # TODO: use iter to create an iterator over a collection
    # day = iter(days)
    # print(next(day))
    # print(next(day))
    # TODO: iterate using a function and a sentinel
    # with open("testfile.txt", 'r') as fp:
    #     for f in iter(fp.readline, ''):
    #         print(f)
    # TODO: use regular interation over the days
    # for day in range(len(days)):
    #     print(days[day])
    # TODO: using enumerate reduces code and provides a counter
    # for daynum, day in enumerate(days, start=1):
    #     print(daynum, day)
    # TODO: use zip to combine sequences
    for daynum, day in enumerate(zip(days, daysFr)):
        print(daynum, day[0], '=', day[1])


if __name__ == "__main__":
    main()
