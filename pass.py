# Python program to show how to use a pass statement in a for loop
'''''pass acts as a placeholder. We can fill this place later on'''
sequence = {"Python", "Pass", "Statement", "Placeholder"}
for value in sequence:
    if value == "Pass":
        pass # leaving an empty if block using the pass keyword
    else:
        print("Not reached pass keyword: ", value)


 # Python program to show how to create an empty function and an empty class
# Empty function:
def empty():
    pass

# Empty class
class Empty:
    pass