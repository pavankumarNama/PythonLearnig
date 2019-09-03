# define enumerations using the Enum base class
from enum import Enum, auto, unique

@unique
class myCustomEnum(Enum):
    MON = auto()
    TUE = auto()
    WED = auto()
    THU = auto()
    FRI = auto()
    SAT = auto()
    SUN = auto()


def main():
    pass
    # TODO: enums have human-readable values and types

    print(repr(myCustomEnum.SUN))
    # TODO: enums have name and value properties
    print(myCustomEnum.MON.name, myCustomEnum.MON.value)
    # TODO: print the auto-generated value
    print(myCustomEnum.SAT.name, myCustomEnum.SAT.value)
    # TODO: enums are hashable - can be used as keys
    weekdays = {}
    weekdays[myCustomEnum.MON.value] = "Monday"
    print(weekdays[myCustomEnum.MON.value])
    print(weekdays)

if __name__ == "__main__":
    main()
