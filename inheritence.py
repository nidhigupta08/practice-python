"""
# SINGLE INHERITENCE
class animal:   # base class
    def eat(self):
        print("Eating")
class dog(animal):    # derived class
    def bark(self):
        print("Barking")
obj=dog()     # object ceated of base class
obj.eat()    # accessing function with help of object using dot operator
obj.bark()
"""
import self

"""
class student:
    def getData(self, roll_no, name, course):
        self.roll_no=roll_no
        self.name=name
        self.course=course
    def displayStudent(self):
        print(" roll no:" ,self.roll_no)
        print("name:", self.name)
        print("course:", self.course)
class test(student):
    def getMarks(self, marks):
        self.marks=marks
    def displayMarks(self):
        print("Total marks:", self.marks)
roll=int(input("Enter roll no:"))
nam=input("Enter your name:")
course_name=input("enter your course name")
mark=int(input("enter your marks"))
# CREATING THE OBJECT
obj=test()
print("displaying result")
obj.getData(roll, nam, course_name)
obj.getMarks(mark)
obj.displayStudent()
obj.displayMarks()
"""
"""
#MULTIPLE INHERITENCE
class student:
    def getData(self, roll_no, name, course):
        self.roll_no=roll_no
        self.name=name
        self.course=course
    def displayStudent(self):
        print(" roll no:" ,self.roll_no)
        print("name:", self.name)
        print("course:", self.course)
# INHERITENCE
class test(student):
    def getMarks(self, marks):
        self.marks=marks
    def displayMarks(self):
        print("Total marks:", self.marks)
class sports:
    def getSportsMarks(self, spmarks):
        self.spmarks=spmarks
    def displaySportMarks(self):
        print("Sports marks:", self.spmarks)
# MULTIPLE INHERITENCE
class result(test,sports):
    def calcilateGrade(self):
        m=self.marks+self.spmarks
        if m>480: self.grade="Distinction"
        elif m>360: self.grade="First class"
        elif m>240: self.grade="Second class"
        else: self.grade="Failed"
    print("Result:", self.grade)
# MAIN PROGRAM
roll=int(input("Enter roll no:"))
nam=input("Enter your name:")
course_name=input("enter your course name")
mark=int(input("enter your marks"))
sprt = int(input("Enter sports marks"))

# CREATING THE OBJECT
obj=result()  # INSTANCE OF CHILD
print("displaying result")
obj.getData(roll, nam, course_name)
obj.getMarks(mark)
obj.getSportsMarks(sprt)
obj.displayStudent()
obj.displayMarks()
obj.displaySportMarks()
obj.calcilateGrade()
"""

