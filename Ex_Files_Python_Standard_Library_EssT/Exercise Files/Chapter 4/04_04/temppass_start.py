# Create a temporary password using Python
import secrets
import string


# TODO: Function to return a temporary password given a length
def generateTempPass(numChars=8):
    temp_pass_chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + "@#$?."
    temp_pass = ''.join(secrets.choice(temp_pass_chars) for digit in range(numChars))
    return temp_pass

# TODO: Function to return a temporary password and enforce 1 number and 1 uppercase
def generateBetterPass(numChars=8):
    temp_pass_chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + "@#$?."
    while True:
        temp_pass = ''.join(secrets.choice(temp_pass_chars) for digit in range(numChars))
        if any(c.isupper() for c in temp_pass) and any(c.isdigit() for c in temp_pass):
            return temp_pass


# create a temporary password
print(generateTempPass(10))

# create a stronger temporary password
print(generateBetterPass(10))


# TODO: create a temporary, hard-to-guess URL
resultUrl = "https://my.example.com?reset="
resultUrl += secrets.token_urlsafe()
print(resultUrl)
