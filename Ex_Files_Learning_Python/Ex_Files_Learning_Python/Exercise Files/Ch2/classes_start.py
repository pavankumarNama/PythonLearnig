#
# Example file for working with classes
#
class firstClass:
  def methodOne(self):
    print("In methodOne")

  def methodTwo(self):
    print("In methodTwo")

class secondClass(firstClass):
  def methodOne(self, args):
    firstClass.methodOne(self)
    print("In secondClass methodOne" + args)

  def methodTwo(self):
    print("In secondClass methodTwo")


def main():
  obj = firstClass()
  obj.methodOne()
  obj.methodTwo()

  objOne = secondClass()
  objOne.methodOne("  Hiii")
  objOne.methodTwo()




if __name__ == "__main__":
  main()
