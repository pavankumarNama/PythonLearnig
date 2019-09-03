#
# Example file for working with functions
#
# def print(*args):
#     print(args)
# define a basic function
func = "I'm function"

def func():
    print("Basic Function")

# function that takes arguments
def add(a, b):
    print(a+b)

# function that returns a value
def sub(a, b):
    print("Sum is", "   ", a-b)
    return a-b
# function with default value for an argument
def multiple(a, b=1):
    return a*b

#function with variable number of arguments
def multisum(*args):
    result = 0
    for i in args:
        result = result + i

    return result



# print(func)
# func()
# print(func())
# print(add())
# print(add(10, 25))
# print(add)
# print(add(-5, 15.2558))
# print(sub(5, 8))
# print(sub)
# print(sub(-10, -10))
# print(multiple(5))
# print(multiple(5, 89))
# print(multiple(10.55, 55.97642))
# print(multiple)
# print(multisum(10, 25, 35, 55, 100, 150))
# print(multisum())