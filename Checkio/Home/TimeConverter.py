from datetime import time


def time_converter(t):
    hr, mt = list(t.split(':'))
    print((int(hr)-1)%12+1)
    tobj = time(hour=int(hr), minute=int(mt))
    time_converter=lambda t:(lambda h,m:f'{(int(h)-1)%12+1}:{m} {"pa"[h<"12"]}.m.')(*t.split(':'))
    # print(time_converter(t))
    if int(hr) >= 12:
        return tobj.strftime("%I:%M")[1:]+' p.m.' if tobj.strftime("%I:%M")[0] == str(0) else tobj.strftime("%I:%M")+' p.m.'
    else:
        return tobj.strftime("%I:%M")[1:]+' a.m.' if tobj.strftime("%I:%M")[0] == str(0) else tobj.strftime("%I:%M")+' a.m.'


if __name__ == '__main__':
    print("Example:")
    print(time_converter('09:00'))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")