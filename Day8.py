#Function
def greet_user():
    print("Hi there!")
    print("welcome aboard")
print("Start")
greet_user()
print("Finish")

def my_function(fname):
  print(fname + " abc")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

def my_function1(fname,lname):
    print(fname + " "+ lname)
my_function1("nidhi","gupta")

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

# Arbitrary Arguments, *args If you do not know how many arguments that will be passed into your function, add a * before the
# parameter name in the  function definition.
#sum of n numbers
def n_no_sum(*num):
    sum=0
    for i in num:
        sum+=i
    return sum
print(n_no_sum(1,2,3,4,5,6,7))