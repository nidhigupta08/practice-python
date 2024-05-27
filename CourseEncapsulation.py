class Course:
    def __init__(self, course_code, title, instructor, credits):
        self.course_code = course_code   # Public attribute
        self.title = title               # Public attribute
        self.instructor = instructor     # Public attribute
        self.__credits = credits         # Private attribute

    def get_credits(self):
        return self.__credits

    def set_credits(self, credits):
        if 0 < credits <= 5:
            self.__credits = credits
        else:
            print("Invalid credit amount!")

    def display_course_details(self):
        print(f"Course Code: {self.course_code}")
        print(f"Title: {self.title}")
        print(f"Instructor: {self.instructor}")
        print(f"Credits: {self.get_credits()}")

# Creating a Course object
course = Course("CS101", "Intro to Computer Science", "Dr. Smith", 3)

# Displaying course details
course.display_course_details()
# Output:
# Course Code: CS101
# Title: Intro to Computer Science
# Instructor: Dr. Smith
# Credits: 3

# Setting new credits
course.set_credits(4)
course.display_course_details()
# Output:
# Course Code: CS101
# Title: Intro to Computer Science
# Instructor: Dr. Smith
# Credits: 4
