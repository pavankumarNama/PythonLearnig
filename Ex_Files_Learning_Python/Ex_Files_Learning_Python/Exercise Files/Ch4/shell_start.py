#
# Example file for working with filesystem shell methods
#
import os
from os import path
import shutil
from zipfile import ZipFile


def main():
  # make a duplicate of an existing file
  if path.exists("samplefile.txt"):
    # get the path to the file in the current directory
    src = path.realpath("samplefile.txt")
    
    # let's make a backup copy by appending "bak" to the name
    shutil.copy(src, src+".bak")

    # copy over the permissions, modification times, and other info
    shutil.copystat(src, src+".bak")

    # rename the original file
    os.rename("samplefile.txt", "examplefile.txt")
    os.rename("examplefile.txt", "samplefile.txt")
    
    # now put things into a ZIP archive
    root, f = path.split(src)
    shutil.make_archive("samplezip", "zip", root)

    # more fine-grained control over ZIP files
    with ZipFile("examplezip.zip", "w") as newzip:
      newzip.write("samplefile.txt")
      newzip.write("samplefile.txt.bak")

if __name__ == "__main__":
  main()
