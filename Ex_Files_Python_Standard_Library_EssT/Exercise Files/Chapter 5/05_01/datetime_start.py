# Basics of dates and times
from datetime import date, time, datetime


# TODO: create a new date object
tdate = date.today()
print(tdate)

# TODO: create a new time object
t = time(15, 20, 20)
print(t)

# TODO: create a new datetime object
dt = datetime.now()
dt1 = datetime.today()
print(dt)
print(dt1)

# TODO: access various components of the date and time objects
print(tdate.year)
print(tdate.month)
print(tdate.weekday())


print(t.hour)
print(t.minute)

# print('--------- ', time.hour)

# TODO: To modify values of date and time objects, use the replace function
d1 = tdate.replace(year=2021, month=12, day=31)
t1 = t.replace(hour=20, minute=33, second=45, microsecond=1000)
dt1 = dt.replace(year=2022, month=11, day=30, hour=14, minute=30, second=55, microsecond=5000)
print(d1)
print(t1)
print(dt1)
