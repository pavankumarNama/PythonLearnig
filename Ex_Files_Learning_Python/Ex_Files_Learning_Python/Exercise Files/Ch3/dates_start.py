#
# Example file for working with date information
#
from datetime import date
from datetime import time
from datetime import datetime

def main(something):
  # DATE OBJECTS
  # Get today's date from the simple today() method from the date class
  today = date.today()
  print("Today Date is :: ", today)

  # print out the date's individual components
  print(today.day, today.month, today.year)

  # retrieve today's weekday (0=Monday, 6=Sunday)
  print(today.weekday())

  
  # DATETIME OBJECTS
  # Get today's date from the datetime class
  today = datetime.now()
  print(something)
  print(today)
  print(today.date())
  # Get the current time
  print(today.time())
  print(datetime.time(datetime.now()))
  print(datetime.date(datetime.now()))


main("Pavan")
if __name__ == "__main__":
  main("Nama")