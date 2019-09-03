#
# Example file for working with timedelta objects
#

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

# construct a basic timedelta and print it
print(timedelta(days=30, hours=12, minutes=30))

# print today's date
now = datetime.now()
print("Today date is : " + str(now))

# print today's date one year from now
print("today's date one year from now is : " + str(now + timedelta(days=365)))

# create a timedelta that uses more than one argument
print(str(now + timedelta(weeks=4, hours=6, minutes=45)))

# calculate the date 1 week ago, formatted as a string
weekAgo = now - timedelta(weeks=1)
print(str(now - timedelta(weeks=1)))
print(weekAgo.strftime("%A %d, %B, %Y"))
### How many days until April Fools' Day?
today = date.today()
afd = date(today.year, 4, 1)
print(today)
print(afd)
# use date comparison to see if April Fool's has already gone for this year
# if it has, use the replace() function to get the date for next year
if afd < today:
    print("It's gone by : " + str((today - afd).days) + "days")
    afd = afd.replace(year=today.year+1)
    print((afd - today).days)
# Now calculate the amount of time until April Fool's Day  


