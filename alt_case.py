def alt_case(text):
    alt_text = ''
    for i in range(len(text)):
        if i % 2 == 0:
            alt_text += text[i].upper()
        else:
            alt_text += text[i]
    return alt_text

# Example usage:
if __name__ == "__main__":
    input_text = input("Enter a text to convert to AltCase: ")
    result = alt_case(input_text)
    print("AltCase text:")
    print(result)
