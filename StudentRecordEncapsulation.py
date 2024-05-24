class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name                  # Public attribute
        self.roll_number = roll_number    # Public attribute
        self.__marks = marks              # Private attribute

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid marks!")

    def display_student_details(self):
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print(f"Marks: {self.get_marks()}")

# Creating a Student object
student = Student("Bob", "S101", 85)

# Displaying student details
student.display_student_details()
# Output:
# Name: Bob
# Roll Number: S101
# Marks: 85

# Setting new marks
student.set_marks(90)
student.display_student_details()
# Output:
# Name: Bob
# Roll Number: S101
# Marks: 90
