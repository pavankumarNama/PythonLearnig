# demonstrate using the random module to create random numbers
import random

# TODO: create a random number
print(random.random())

# TODO: implement a coin toss function
[print("Heads") if random.random() < 0.5 else print("Tails") for i in range(10)]

# TODO: get a random number within a range
print(random.uniform(10, 100))

# TODO: generate random integers within a given range
print(random.randint(10, 100))

# TODO: generate random integers with a step function
# this example chooses from 0 to 100 stepped by 5
print(random.randrange(10, 100, 5))

# TODO: Use the seed function to position the generator
random.seed(16)
print(random.randint(1, 1000))
random.seed(3)
print(random.randint(1, 1000))
print("----------------")
