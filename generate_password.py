import random
import string

def generate_password(length):
    # Define characters to be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the password using random choices from the characters
    password = ''.join(random.choices(characters, k=length))

    return password

# Taking input for the desired length of the password
password_length = int(input("Enter the length of the password: "))

# Generating the password
password = generate_password(password_length)

print("Generated Password:", password)
