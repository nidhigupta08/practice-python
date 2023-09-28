#Function
def greet_user():
    print("Hi there!")
    print("welcome aboard")
print("Start")
greet_user()
print("Finish")

def my_function(fname):   #parameters receive information
  print(fname + " abc")

my_function("Emil")  #arguments which we supply to the func.
my_function("Tobias")
my_function("Linus")

# (fname write clk +refactor+ rename  |||||||||||||||||||  shift+f6)  ---->>.rename dialogue box.
def my_function1(fname,lname):
    print(fname + " "+ lname)
my_function1("nidhi","gupta")  # also called positional argument

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

# def sum_squares(*args):
#     return sum(args**0.5)
# print(sum_squares(5,6,7))

def sum_square(*num):
    sum=0
    for i in num:
        sum+=i**2
    return sum
print(sum_square(2,3,4))

def sum_squares(*args):
  """Returns the sum of the squares of the arguments.

  Args:
    *args: Any number of numeric arguments.

  Returns:
    The sum of the squares of the arguments.
  """
  sum_of_squares = 0
  for arg in args:
    sum_of_squares += arg ** 2
  return sum_of_squares
print(sum_squares(1, 2, 3))
print(sum_squares(10,20,30))

def square(num):
    return num*num
print(square(4))

