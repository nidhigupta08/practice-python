# Define lists of word types
nouns = ["dog", "cat", "dinosaur", "teacher"]
verbs = ["jumped", "sang", "slept", "danced"]
adjectives = ["happy", "sad", "angry", "silly"]
adverbs = ["quickly", "slowly", "loudly", "softly"]

# Define the story template
story = f"Once upon a time, there was a {adjectives[0]} {nouns[0]} who {verbs[0]} {adverbs[0]}."

# Get user input for different word types
user_noun = input("Enter a noun: ")
user_verb = input("Enter a verb: ")
user_adjective = input("Enter an adjective: ")
user_adverb = input("Enter an adverb: ")

# Insert user input into the story template
story = story.replace("[0]", user_adjective)  # Assuming positions in list match template placeholders (can be improved for more flexibility)
story = story.replace("[1]", user_noun)
story = story.replace("[2]", user_verb)
story = story.replace("[3]", user_adverb)

# Print the completed story
print(story)
