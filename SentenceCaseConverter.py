def sentence_case(text):
    # Convert the text to lowercase first
    text = text.lower()

    # Split the text into sentences
    sentences = text.split('. ')

    # Capitalize the first letter of each sentence
    capitalized_sentences = [sentence.capitalize() for sentence in sentences]

    # Join the sentences back together
    sentence_case_text = '. '.join(capitalized_sentences)

    # Capitalize the first letter of the entire string
    sentence_case_text = sentence_case_text.capitalize()

    return sentence_case_text

# Example usage:
if __name__ == "__main__":
    input_text = input("Enter a text to convert to sentence case: ")
    result = sentence_case(input_text)
    print("Sentence case text:")
    print(result)


