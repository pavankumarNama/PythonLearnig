# Using cryptographic-appropriate methods to generate random data
# that may be sensitive. secrets module introduced in Python 3.6
import os
import secrets


# TODO: the urandom() function in the OS module produces random numbers that
# are cryptographically safe to use for sensitive purposes
for i in os.urandom(5):
    print(hex(i))

# TODO: secrets.choice is the same as random.choice but more secure
moves = ["rock", "paper", "scissors"]
print(secrets.choice(moves))

# TODO: secrets.token_bytes generates random bytes
print(secrets.token_bytes())

# TODO: secrets.token_hex creates a random string in hexadecimal
print(secrets.token_hex())

# TODO: secrets.token_urlsafe generates characters that can be in URLs
print(secrets.token_urlsafe())
