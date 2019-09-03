#
# Example file for working with loops
#

def main():
  x = 0

  # define a while loop
  # while (x < 5):
  #   print(x)
  #   x = x+1

  # define a for loop
  # for x in range(5):
  #   print(x)

  # for x in range(5, 15, 2):
  #   print(x)

  # use a for loop over a collection
  # numbers = [10, 22, 33, 43, 45]
  # for i in numbers:
  #   print(i)
  # use the break and continue statements
  # for a in range(5, 15):
  #   if(a == 10):
  #     break
  #
  #   if(a%3 == 0):
  #     continue
  #
  #   print(a)

  #using the enumerate() function to get index 
  numbers = [10, 22, 33, 43, 45]
  for a,b in enumerate(numbers):
    print(a, " - ", b)

if __name__ == "__main__":
  main()
