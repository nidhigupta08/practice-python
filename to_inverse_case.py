def to_inverse_case(text):
    result = ''
    for char in text:
        if char.isupper():
            result += char.lower()
        else:
            result += char.upper()
    return result

# Test the function
text = input("Enter the text: ")
inverse_case_text = to_inverse_case(text)
print("Text in inverse case:", inverse_case_text)
