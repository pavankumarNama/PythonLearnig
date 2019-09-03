#
# Read and write files using the built-in Python file methods
#

def main():  
  # Open a file for writing and create it if it doesn't exist
  # f = open("samplefile.txt", "w+")
  # for i in range(10):
  #   f.write("Line number : " + str(i) + "\r\n")
  # Open the file for appending text to the end
  # f = open("samplefile.txt", "a")


  # write some lines of data to the file
  # for i in range(10, 20):
  #   f.write("Line number : " + str(i) + "\r\n")
  # close the file when done
  # f.close()
  
  # Open the file back up and read the contents
  f = open("samplefile.txt", "r")

  if f.mode == "r":
    f1 = f.readlines()

    for i in f1:
      print(i)

  f.close()
    
if __name__ == "__main__":
  main()
