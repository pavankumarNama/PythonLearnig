#
# Example file for working with Calendars
#

# import the calendar module
import calendar

# create a plain text calendar
# cal = calendar.TextCalendar(calendar.MONDAY)
# print(cal.formatmonth(2019, 7, 0, 0))

# create an HTML formatted calendar
# cal = calendar.HTMLCalendar(calendar.MONDAY)
# print(cal.formatmonth(2018, 1))
# loop over the days of a month
# zeroes mean that the day of the week is in an overlapping month
# for days in cal.itermonthdays(2019, 7):
#     print(days)
  
# The Calendar module provides useful utilities for the given locale,
# such as the names of days and months in both full and abbreviated forms
# for month in calendar.month_name:
#     print(month)
# for day in calendar.day_name:
#     print(day)
# Calculate days based on a rule: For example, consider
# a team meeting on the first Friday of every month.
# To figure out what days that would be for each month,
# we can use this script:
# print ("Team meetings will be on:")
# for m in range(1, 13):
#     cal = calendar.monthcalendar(2019, m)
#     weekone = cal[0]
#     weektwo = cal[1]
#
#     if weekone[calendar.FRIDAY] != 0:
#         meetday = weekone[calendar.FRIDAY]
#     else:
#         meetday = weektwo[calendar.FRIDAY]
#
#     print ("%10s %2d" % (calendar.month_name[m], meetday))

print(calendar.monthcalendar(2019, 1)[calendar.SUNDAY])