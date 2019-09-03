#
# Example file for working with os.path module
#
import os
from os import path
import datetime
from datetime import date, time, timedelta
import time


def main():
  # Print the name of the OS
  print(os.name)

  # Check for item existence and type
  print(path.exists("samplefile.txt"))
  print(path.isfile("samplefile.txt"))
  print(path.isdir("samplefile.txt"))
  print(path.isabs("samplefile.txt"))
  print(path.islink("samplefile.txt"))
  print(path.ismount("samplefile.txt"))

  # Work with file paths
  print(path.realpath("samplefile.txt"))
  print(path.split(path.realpath("samplefile.txt")))
  # Get the modification time
  mt = time.ctime(path.getmtime("samplefile.txt"))
  print(mt)
  print(datetime.datetime.fromtimestamp(path.getmtime("samplefile.txt")))
  
  # Calculate how long ago the item was modified
  td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("samplefile.txt"))
  print(td)
  print(td.total_seconds())

  
if __name__ == "__main__":
  main()
