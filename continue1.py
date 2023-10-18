# Python Continue Statements in while Loop

# Creating a string
string = "Nidhiaguptaman"
# initializing an iterator
iterator = 0

# starting a while loop
while iterator < len(string):
    # if loop is at letter a it will skip the remaining code and go to next iteration
    if string[iterator] == 'a':
        iterator += 1  # Increment the iterator here
        continue
    # otherwise it will print the letter
    print(string[iterator])
    iterator += 1