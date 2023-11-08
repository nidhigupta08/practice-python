def is_palindrome(s):
    return s == s[::-1]

def find_smallest_palindrome():
    user_input = input("Enter a string: ")
    user_input = user_input.lower()  # Convert the input to lowercase for case insensitivity
    user_input = ''.join(filter(str.isalnum, user_input))  # Remove non-alphanumeric characters

    # Check if the input is already a palindrome
    if is_palindrome(user_input):
        return user_input

    for i in range(1, len(user_input)):
        substr = user_input[:i]
        if is_palindrome(substr):
            return substr

    return "No palindrome substring found"

smallest_palindrome = find_smallest_palindrome()
print("The smallest palindrome substring is:", smallest_palindrome)
