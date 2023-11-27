# First parent class
class Chef:
    def __init__(self, cuisine):
        self.cuisine = cuisine

    def cook(self):
        return "Cooking delicious food!"

# Second parent class
class Teacher:
    def __init__(self, subject):
        self.subject = subject

    def teach(self):
        return "Teaching students!"

# Child class inheriting from Chef and Teacher
class MultitalentedPerson(Chef, Teacher):
    def __init__(self, cuisine, subject):
        Chef.__init__(self, cuisine)
        Teacher.__init__(self, subject)

# Creating an instance of MultitalentedPerson class
renaissance_person = MultitalentedPerson('Italian', 'Mathematics')

# Accessing attributes and methods
print(f"This person specializes in {renaissance_person.cuisine} cuisine.")
print(f"They teach {renaissance_person.subject}.")
print(renaissance_person.cook())
print(renaissance_person.teach())
