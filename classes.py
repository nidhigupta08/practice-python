class data :
    pass
obj = data()
print(type(obj))


class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
obj1 = person("nidhi", 20)
print(obj1.name)
print(obj1.age)


class car:
    speed=0
    color="white"
    def increase_speed(self):
        self.speed+= 10
tesla=car()
tesla.color="black"

print(tesla.color)
print(tesla.speed)
tesla.increase_speed()
print(tesla.speed)


class myclass:
    def method1(self):
        print("Nirali prakashan")
    def method2(self, someString):
        print("Software testing:"+ someString)
def main():
    obj = myclass ()
    obj.method1 ()
    obj.method2("testing is fun")
if __name__=="__main__":
    main()

class employee:
    'common base class for all employee'
    empCount = 0
    def __init__(self, name, salary):
        self.name= name
        self.salary = salary
        employee.empCount+=1
    # def displayCount(self):
    #     print( "total employee %d" % employee.empCount)
    def displayEmployee(self):
        print("Name:", self.name, ",Salary:", self.salary)

"this would create 1st object of employee class"
obj1 = employee("Nidhi", 50000)
"this would create 2nd object of employee class"
obj2 = employee("Suman", 50000)
obj3 = employee("Deeps", 50000)
obj1.displayEmployee()
obj2.displayEmployee()
obj3.displayEmployee()
# print("Total employee %d",% employee.empCount)
print("total employee %d" % employee.empCount)
