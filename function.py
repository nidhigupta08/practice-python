# a = 5
# b = 5
# c = sum((a, b))  # built-in function
# print(c)

# user define-function-to use this we have to use "def"
# def func1():
#     print("Hello function ")
#     func1()

# def func2(a, b):
#     print(a+b)
# func2(2, 4)

# def func3(a, b):
#     """docstring"""
#     average = (a+b)/2
#     # print(average)
#     return average
# # avg=func3(3,5) this without return statement i can't store a value in any variable
# avg = func3(3, 5)
# print(avg)
#
# def greet(name):
#     """This function greets to the person passed in as a parameter """
#     print("Hello, " + name + ". Good morning!")
# greet('Nidhi')
# print(greet.__doc__)

# def absolute_value(num):
#     """This function returns the absolute value of the entered number"""
#     if num >= 0:
#         return num
#     else:
#         return num
# print(absolute_value(2))
# print(absolute_value(-4))

# Recursion is a common mathematical and programming concept.
# def tri_recursion(k):
#   if(k > 0):
#     result = k + tri_recursion(k - 1)
#     print(result)
#   else:
#     result = 0
#   return result
#
# print("\n\nRecursion Example Results")
# tri_recursion(6)


x = "awesome"

def fun5():
  x = "fantastic"
  print("pythonn is " + x)

fun5()
print("python is " + x)




