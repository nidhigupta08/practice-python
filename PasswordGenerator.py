import random

# Define password criteria
min_length = 8
max_length = 16
lowercase = True
uppercase = True
numbers = True
symbols = "!@#$%^&*"

# Generate random password based on criteria
def generate_password():
    # Define character sets based on user criteria
    char_set = ""
    if lowercase:
        char_set += "".join(chr(i) for i in range(ord('a'), ord('z') + 1))
    if uppercase:
        char_set += "".join(chr(i) for i in range(ord('A'), ord('Z') + 1))
    if numbers:
        char_set += "".join(str(i) for i in range(10))
    if symbols:
        char_set += symbols

    # Ensure char_set is not empty
    if not char_set:
        return "No characters available to generate password."

    # Generate random password with desired length
    password_length = random.randint(min_length, max_length)
    password = "".join(random.choice(char_set) for _ in range(password_length))
    return password

# Generate and print a password
password = generate_password()
print(f"Your generated password is: {password}")
