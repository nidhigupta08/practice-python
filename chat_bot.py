import random

# Dictionary mapping user input to bot responses
responses = {
    "hello": ["Hi there!", "Hello!", "Hey!"],
    "how are you": ["I'm doing well, thank you!", "I'm good, thanks for asking!", "I'm fine, how about you?"],
    "goodbye": ["Goodbye!", "See you later!", "Bye!"],
    "thanks": ["You're welcome!", "No problem!", "Anytime!"],
    "default": ["Sorry, I didn't understand that.", "Could you please repeat that?", "I'm not sure what you mean."]
}

def chat():
    print("Welcome! Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ").lower()
        if user_input == 'exit':
            print("Bot: Goodbye!")
            break
        bot_response = responses.get(user_input, responses["default"])
        print("Bot:", random.choice(bot_response))

# Run the chatbot
chat()
