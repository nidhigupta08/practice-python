#passcal naming convention
class Point:
    def __init__(self,x,y): #parameter. to initilize an object self.x=x. Self is the reference to the current object.
        #this is a constructor to contruct an object.
        self.x=x
        self.y=y

    def move(self):
        print("move")
    def draw(self):
        print("draw")

point1=Point()
point1.x=10
point1.y=20
print(point1.x)
point1.draw()

point2=Point(10,20) #argument
point2.x=12
print(point2.x)

# define class person and  attribute as name  and method as talk()
class Person:
    def __init__(self,name): # setting the name attribute of the cureent object  to the name argument passed to this method
        self.name=name
    def talk(self):
        print("i m talking keep quiet.")
        print(f" Hi my name is {self.name}")


person=Person("nidhi")
print(person.name)
person.talk()

bob=Person("gupta nidhi")
bob.talk()
# each object is different instance of the person class.
