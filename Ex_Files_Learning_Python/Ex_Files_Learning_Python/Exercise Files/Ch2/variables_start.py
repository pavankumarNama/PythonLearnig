# 
# Example file for variables
#

# Declare a variable and initialize it
a = 10
print(a)

# # re-declaring the variable works
a = 15.58
print(a)

# # ERROR: variables of different types cannot be combined
print(10 + 55.56 + -51.566)
print('variable value is : ' + str(a) + '.')

# Global vs. local variables in functions


def fun():
    global a
    a = "Hello"
    print(a)


fun()


print(a)

del a

print(a)