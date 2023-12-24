# Lists are used to store multiple items in a single variable.
# 4 built-in data types in Python--1 is list and 3 are Tuple, Set, and Dictionary,
# Lists are created using square brackets:
# List items are ordered, changeable, and allow duplicate values.
# List items can be of any data type:

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

# list = ["nidhi", "piku", "Suman", 7, 33, 8]
# tropical = ["mango", "pineapple", "papaya"]
# list.extend(tropical)  # append the both list
# print(list)
# print(len(list))
# print(list[1])
# list.insert(2, "watermelon")
# print(list)
# list.remove(7)
# print(list)
# for i in list:
#     print(i)
#
# for i in range(2):   # nidhi, piku
#     print(list[i])

#  Loop Through the Index Numbers using range() and len() functions.
# for i in range(len(list)):
#     print(list[i])

# len() function to determine the length of the list
# WHILE LOOP
# i = 0
# while i < len(list):
#     print(list[i])
#     i = i+1
# List Comprehension offers the shortest syntax for looping through lists:

# list2 = ["mango", "papaya", "chiku", "kiwi"]
# [print(i) for i in list2]

# Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
#  below program has done using for loop
# newlist = []
# for i in list2:
#     if "a" in i:
#         newlist.append(i)
# print(newlist)

# using list comprehension  ::::::::::::newlist = [expression for item in iterable if condition == True]
# newlist1 = [i for i in list2 if "a" in i]
# print(newlist1)

# list2.sort()                  Ascending order acc. to alphabets
# print(list2)

# list2.sort(reverse=True)       # Descending order acc. to alphabets
# print(list2)

# list2.reverse()  # reverse the order of the list
# print(list2)

# Copy a List
# on way  to copy ----built - in List method copy().

# thislist = ["apple", "banana", "cherry"]
# mylist = thislist.copy()
# print(mylist)

# 2nd way to copy is  use the built-in method list().
# thislist1 = [" apple", "kiwi", "orange"]
# mylist = list(thislist1)
# print(mylist)

# Join Two Lists
# 1 way
# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]
#
# list3 = list1 + list2
# print(list3)

# 2nd way --appending all the items from list2 into list1
# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]
#
# for i in list2:
#   list1.append(i)
# print(list1)


# extend()method-add elements from one list to another
# list1 = ["a", "b", " c", "a"]
# list2 = [1, 2, 3]
# list1.extend(list2)
# print(list1)

# using count() method -return no of times cherry appears in fruits list
# fruits = ['apple', 'banana', 'cherry', "apple"]
# x = fruits.count("apple")
# print(x)

# list.count(value)
# Value--Required. Any type (string, number, list, tuple, etc.). The value to search for.


fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
print(fruits)
