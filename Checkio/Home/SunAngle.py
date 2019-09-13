from datetime import time as s_time

def sun_angle(time):
    #replace this for solution
    hr, mt = time.split(':')
    tobj = s_time(hour=int(hr), minute=int(mt))
    r_time = tobj.strftime("%H:%M")
    sun_raise = s_time(hour=6, minute=0).strftime("%H:%M")
    sun_set = s_time(hour=18, minute=0).strftime("%H:%M")
    # print(r_time)
    # print(sun_raise.__class__)
    # print(sun_set.__class__)
    # one hour = 15 degrees
    onehr = 15
    # one minute = 0.25 degrees
    onemt = 0.25
    return (int(hr) - 6) * onehr + int(mt) * onemt if sun_raise <= r_time <= sun_set else "I don't see the sun!"


if __name__ == '__main__':
    # print("Example:")
    # print(sun_angle("07:00"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")