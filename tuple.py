# Tuples are used to store multiple items in a single variable.
# Tuple items are ordered, unchangeable, and allow duplicate values.
# Tuples are unchangeable, or immutable

tuple1 = ("Apple", "Bnanana", "cherry")
print(tuple1)  # ('Apple', 'Bnanana', 'cherry')
print(len(tuple1))  # 3

tuple2 = ("apple",)
print(type(tuple2))  # <class 'tuple'>

tuple2 = ("apple")
print(type(tuple2))   # <class 'str'>

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
print(tuple1)
print(tuple2)
print(tuple3)

tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)

# use the tuple() constructor to make a tuple.
thistuple = tuple(("apple", "banana", "cherry", "kiwi", "melon", "orange"))  # note the double round-brackets
print(thistuple)
print(thistuple[1])
print(thistuple[2:5])

if "apple" in thistuple:
    print("yes, 'apple' is in the thistuple")


#  ADD ITEMS IN TUPLE

# Tuples are unchangeable, or immutable
# You can convert the tuple into a list, change the list,
# and convert the list back into a tuple.

# 1)   Convert into a list:
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

# Convert the tuple into a list, add "orange", and convert it back into a tuple:
tuple3 = ("Apple ", "kiwi", "banana", "dragon fruits")
convert_list = list(tuple3)
convert_list.append("orange")
tuple3 = tuple(convert_list)
print(tuple3)


# 2)  ADD TUPLE TO A TUPLE
# You are allowed to add tuples to tuples, so if you want to add one item,
# (or many), create a new tuple with the item(s),
# and add it to the existing tuple:

tuple4 = ("mango", "apple", "kiwi", "chikku")
tuple5 = ("orange",)
tuple4 += tuple5
print(tuple4)

# Tuples are unchangeable, so you cannot remove items from it,
# EXAMPLE: Convert the tuple into a list, remove "apple", and convert it back into a tuple
tuple4 = ("mango", "apple", "kiwi", "chikku")
y = list(tuple4)
y.remove("apple")
tuple4 = tuple(y)
print(tuple4)

# The del keyword can delete the tuple completely:
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple)  # this will raise an error because the tuple no longer exists

# Using Asterisk* ---If the number of variables is less
# than the number of values, you can add an * to the variable
# name and the values will be assigned to the variable as a list:
# Assign the rest of the values as a list called "red":

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(a, b, *c) = fruits
print(a)
print(b)
print(c)

# LOOP THROUGH A TUPLE
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
for i in fruits:
    print(i)

# Loop Through the Index Numbers
for i in range(len(fruits)):
    print(fruits[i])

a = ("apple")
for i in range(len(a)):
    print(a[i])

# Using a While Loop
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
i = 0
while i < len(fruits):
    print(fruits[i])
    i = i + 1


# To join two or more tuples you can use the + operator:
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

# If you want to multiply the content of a tuple a given number
# of times, you can use the * operator:
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

# Tuple Methods ---Python has two built-in methods that you can use on tuples.
# count()
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5)
print(x)  #  return 2


# index()-searches the tuple for a specified value and returns the position
# of where it was found.
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(8)
print(x)  # return 3



# Use the correct method to add multiple items
# (more_fruits) to the fruits set.

fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
