"""Extracting Sub-Strings Practice #1
Extract the first word of the following sentence using slicing, and display it on the screen:
"Controlling complexity is the essence of programming"
Hint: "Controlling" is 11 characters long."""
sentence = "Controlling complexity is tshe essence of programming"
fragment = sentence[0:11]
print(fragment)

""""Extracting Sub-Strings Practice #2
Take every third character starting from the ninth to the end of the sentence, and print the result.
"Never trust a computer you can't throw out a window"""
sentence = "Never trust a computer you can't throw out a window"
fragment = sentence[8::3]
print(fragment)

"""Extracting Sub-Strings Practice #3
Reverses the position of all the characters in the following sentence and displays the result on the screen.
"It's great to work with computers. They don't argue, they remember everything and they don't drink your beer"""
sentence = "It's great to work with computers. They don't argue, they remember everything and they don't drink your beer"
fragment = sentence[::-1]
print(fragment)

