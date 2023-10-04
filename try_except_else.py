n = 10
m = 0
try:
    n/m
except ZeroDivisionError:
    print("divide by zero which will return ZeroDivisionError")
else:
    print(n/m)


# TRY-EXCEPT STATEMENT WITH NO EXCEPTION
while True:
    try:
        a = int(input("enter an integer: "))
        div = 10/a
        break
    except:
        print("Error occurred")
        print("please enter valid value")
        print()
print("division is:", div)


# MULTIPLE EXCEPTIONS
try:
    a = 10/1;
except (ArithmeticError, StandardError):
    print("Arithmetic exception")
else:
    print ("successfully done")


# RAISE STATEMENT
age = int(input("Enter your age for election:"))
try:
    if age < 18:
        raise Exception
    else:
        print("You are eligible for election")
except Exception:
    print("you are too small for voting")

# TRY-FINALLY CLAUSE
try:
    fh = open("testfile", "w")
    try:
        fh.write("This is my test file for exception handlings !")
    finally:
        print("Going to close the file")
    fh.close()
except IOError:
    print("Error: can\'t find file or read data")


# CUSTOM EXCEPTION   or user defined exception
class myerror(Exception):
#  CONSTRUCTOR OR INITIALIZER
    def __init__(self, value):
        self.value=value
# __STR__ IS TO PRINT() THE VALUE
    def __str__(self):
        return(repr(self.value))
try:
    raise(myerror(3*2))
# value of exception is stored in eroor
except myerror as error:
    print('A new exception occured:',error.value)

