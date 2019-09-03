# Demonstrate the usage of OrderedDict objects

from collections import OrderedDict


def main():
    # list of sport teams with wins and losses
    sportTeams = [("Royals", (18, 12)), ("Rockets", (24, 6)), 
                ("Cardinals", (20, 10)), ("Dragons", (22, 8)),
                ("Kings", (15, 15)), ("Chargers", (20, 10)), 
                ("Jets", (16, 14)), ("Warriors", (25, 5))]

    # sort the teams by number of wins
    sortedTeams = sorted(sportTeams, key=lambda t: t[1][0], reverse=True)
    print(sortedTeams)
    # TODO: create an ordered dictionary of the teams
    s1 = OrderedDict(sportTeams)
    print(s1)
    # TODO: Use popitem to remove the top item
    a, b = s1.popitem()
    print(a, b)
    # TODO: What are next the top 4 teams?
    for i, j in enumerate(s1, start=1):
        print(i, j)

    # TODO: test for equality
    a = OrderedDict({"a": 1, "b": 2, "c": 3})
    b = OrderedDict({"a": 1, "c": 3, "b": 2})
    print("Equality test: ", a == b)


if __name__ == "__main__":
    main()
