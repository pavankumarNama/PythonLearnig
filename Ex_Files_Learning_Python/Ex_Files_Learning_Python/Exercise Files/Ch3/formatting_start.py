#
# Example file for formatting time and date output
#

from datetime import datetime

def main():
  # Times and dates can be formatted using a set of predefined string
  # control codes 
  today = datetime.now()
  #### Date Formatting ####
  # print(today)
  # %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month
  # print(today.strftime("%y %Y, %a %A, %b %B, %d"))

  # %c - locale's date and time, %x - locale's date, %X - locale's time
  print(today.strftime("local Date and Time is : %c"))
  print(today.strftime("local Date is : %x"))
  print(today.strftime("local Time is : %X"))

  #### Time Formatting ####
  
  # %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
  print(today.strftime("Date and Time in 12hr Format : %I:%M:%S %p"))
  print(today.strftime("Date and Time in 24hr Format : %H:%M:%S"))


if __name__ == "__main__":
  main();
