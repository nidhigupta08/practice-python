#TUPLES-- it is similar to list and we can use it to stored list of items. it is immutable, we cannot add new items or modified anything..
numbers=(1,2,3,4,7,1)
print(numbers.count(1)) # it is counting or occurence of 1.
print(numbers.index(2)) # the index of 2 is 1.
print(numbers[4])

# SWAPPING OF NUMBER
#but in python there is shortcut which shown below
a = 6
b = 5
# a, b = b, a
# print(a, b)
  #                 OOOOOOOOOOORRRRRRRRRRRR
# Swapping using a temporary variable
temp = a
a = b
b = temp
print(a, b)

num1=12
num2=2
print('before swapping num1:', num1, 'num2: ',num2)
num1=num1+num2
num2=num1-num2
num1=num1-num2
print('after swapping num1:', num1 ,'num2: ',num2)

# Python program to show how to create a tuple
# Creating an empty tuple
empty_tuple = ()
print("Empty tuple: ", empty_tuple)

# Creating tuple having integers
int_tuple = (4, 6, 8, 10, 12, 14)
print("Tuple with integers: ", int_tuple)

# Creating a tuple having objects of different data types
mixed_tuple = (4, "Python", 9.3)
print("Tuple with different data types: ", mixed_tuple)

# Creating a nested tuple
nested_tuple = ("Python", {4: 5, 6: 2, 8: 2}, (5, 3, 5, 6))
print("A nested tuple: ", nested_tuple)


# Python program to show how slicing works in Python tuples
# Creating a tuple
tuple_ = ("Python", "Tuple", "Ordered", "Immutable", "Collection", "Objects")
# Using slicing to access elements of the tuple
print("Elements between indices 1 and 3: ", tuple_[1:3])
# Using negative indexing in slicing
print("Elements between indices 0 and -4: ", tuple_[:-4])
# Printing the entire tuple by using the default start and end values.
print("Entire tuple: ", tuple_[:])


# Creating tuples
Tuple_data = (0, 1, 2, 3, 2, 3, 1, 3, 2)
# getting the index of 3
res = Tuple_data.index(3)
print('First occurrence of 1 is', res)
# getting the index of 3 after 4th
# index
res = Tuple_data.index(3, 4)
print('First occurrence of 1 after 4th index is:', res)
