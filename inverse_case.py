def inverse_case(text):
    inverse_text = ''
    for char in text:
        if char.islower():
            inverse_text += char.upper()
        elif char.isupper():
            inverse_text += char.lower()
        else:
            inverse_text += char
    return inverse_text

# Example usage:
if __name__ == "__main__":
    input_text = input("Enter a text to convert to inverse case: ")
    result = inverse_case(input_text)
    print("Inverse case text:")
    print(result)
