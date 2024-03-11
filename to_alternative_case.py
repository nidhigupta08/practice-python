def to_alternative_case(text):
    result = ''
    for i in range(len(text)):
        char = text[i]
        if i % 2 == 0:
            result += char.upper()
        else:
            result += char.lower()
    return result

# Test the function
text = input("Enter the text: ")
alternative_case_text = to_alternative_case(text)
print("Text in alternative case:", alternative_case_text)
