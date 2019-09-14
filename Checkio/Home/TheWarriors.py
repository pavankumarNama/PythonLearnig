class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5
        self.is_alive = True


class Knight(Warrior):
    def __init__(self):
        self.health = 50
        self.attack = 7
        self.is_alive = True


def fight(unit_1, unit_2):
    f1, f2 = 0, 0
    while True:

        if f1 == 0 and unit_2.health > 0 and unit_1.health > 0:
            f1 = 1
            f2 = 0
            unit_2.health -= unit_1.attack
            # print('unit2: ', unit_2.__class__, unit_2.health)
            continue

        if f2 == 0 and unit_1.health > 0 and unit_2.health > 0:
            f2 = 1
            f1 = 0
            unit_1.health -= unit_2.attack
            # print('unit1: ', unit_1.__class__, unit_1.health)
            continue
        break
    unit_1.is_alive = unit_1.health > 0
    unit_2.is_alive = unit_2.health > 0
    # print(unit_1.health, unit_1.is_alive)
    # print(unit_2.health, unit_2.is_alive)
    # print(True if type(unit_1) == Warrior and unit_1.is_alive else type(unit_2) == Warrior and unit_2.is_alive)
    return True if unit_1.is_alive else False


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()
    assert fight(chuck, bruce) == True
    # print('chunk health: ', chuck.health, chuck.is_alive)
    # print('bruce health: ', bruce.health, bruce.is_alive)
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    # print(bruce.is_alive, bruce.health)
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    # assert fight(carl, mark) == False
    # assert carl.is_alive == False

    print("Coding complete? Let's try tests!")
