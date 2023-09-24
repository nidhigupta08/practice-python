"""String Methods Practice #1
Print the following text in uppercase, using the specific string method:
Especially in electronic communications, writing in all caps is equivalent to yelling."""
sentence = "Especially in electronic communications, writing in all caps is equivalent to yelling."
result = sentence.upper()
print(result)

"""String Methods Practice #2
Join the following list into a string, separating each item with a space. Use the appropriate list/string method, and display the result."""

word_list = ["Simple","is","better","than","complex."]
e = " ".join(word_list)
print(e)

"""String Methods Practice #3
Replace in the following sentence:
"If the implementation is hard to explain, it might be a bad idea."
the following pairs of words:
"hard" --> "easy"
"bad" --> "good"
and display the sentence with both words modified."""

word_list="If the implementation is hard to explain, it might be a bad idea."
e = word_list.replace("hard", "easy").replace("bad", "good")
print(e)