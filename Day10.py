class Animals:
    def walk(self):
        print("walk")


class Dog(Animals):
    def bark(self):
        print("dog barks")


class Goat(Animals):
    pass


class Cat(Animals ):
    def sound(self):
        print("meow")


dog1=Dog()
dog1.walk()

cat=Cat()
cat.walk()
cat.sound()


# The five types of inheritance in Python are single, multiple, multilevel, hierarchical, and hybrid inheritance
# Multi-Level inheritance Multi-level inheritance is archived when a derived class inherits another derived class.
class Animal:
    def speak(self):
        print("Animal Speaking")


#The child class Dog inherits the base class Animal
class Dog(Animal):
    def bark(self):
        print("dog barking")


#The child class Dogchild inherits another child class Dog
class DogChild(Dog):
    def eat(self):
        print("Eating bread...")


d = DogChild()
d.bark()
d.speak()
d.eat()

# Python provides us the flexibility to inherit multiple base classes in the child class.
class Calculation1:
    def Summation(self,a,b):
        return a+b;


class Calculation2:
    def Multiplication(self,a,b):
        return a*b;


class Calculation3:
    def minus(self,a,b):
        return a-b

class Derived(Calculation1,Calculation2):
    def Divide(self,a,b):
        return a/b;


class Derived2(Calculation1,Calculation2,Calculation3):
    def modulas(self,a,b):
        return a % b


d = Derived()
print(d.Summation(10,20))
print(d.Multiplication(10,20))
print(d.Divide(10,20))

derived2=Derived2()
print(derived2.Summation(10,10))
print(derived2.Multiplication(2,2))
print(derived2.minus(10,5))
print(derived2.modulas(10,2))

