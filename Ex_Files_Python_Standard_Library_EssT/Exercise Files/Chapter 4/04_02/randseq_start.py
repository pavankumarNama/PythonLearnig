# Functions for generating random data sequences
import random
import string

# TODO: Use the choice function to randomly select from a sequence
from collections import Counter

moves = ["rock", "paper", "scissors"]
print(random.choice(moves))

# TODO: Use the choices function to create a list of random elements
roulette_wheel = ["black", "red", "green"]
lrandomele = [random.choice(roulette_wheel) for i in range(10)]
print(lrandomele)
print(Counter(lrandomele))
weights = [10, 5, 5]
print(Counter(random.choices(roulette_wheel, weights, k=15)))

# TODO: The sample function randomly selects elements from a population
# without replacement (the chosen items are not replaced)
s = {1, 2, 3, 4, 5}
print(random.sample(s, 5))
print(random.sample(roulette_wheel, k=3))
print(random.sample(string.ascii_uppercase, 10))

# TODO: The shuffle function shuffles a sequence in place
players = ["Bill", "Jane", "Joe", "Sally", "Mike", "Lindsay"]
random.shuffle(players)
print(players)

# TODO: to shuffle an immutable sequence, use the sample function first
name = 'PavanKumarNama'
result = random.sample(name, len(name))
print(result)
random.shuffle(result)
print(result)