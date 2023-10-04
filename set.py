# *********SET***********
# Sets are used to store multiple items in a single variable.
# A set is a collection which is unordered, unchangeable*, and unindexed.
# Set items are unchangeable, but you can remove items and add new items.
# Sets are written with curly brackets.
# Set items are unordered, unchangeable, and do not allow duplicate values.
# Set items can appear in a different order every time you use them, and cannot be referred to by index or key.
# Set items can be of any data type:

this_set = {"apple", "banana", "cherry"}
print(len(this_set))

# String, int and boolean data types:
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
set4 = {"abc", 34, True, 40, "male"}
print(set1, set2,set3)
print(set4)
print(type(set1))

# The set() Constructor
set5 = set(("apple", "banana", "cherry"))
print(set5)

set6 = {"apple", "banana", "cherry"}
for i in set6:
    print(i)
if "banana" in set6:   # not allowed in set
    print("yes, it is present .")
print("banana" in set6)
#
set6.add("orange")
print(set6)
# To add items from another set
# into the current set, use the update() method
set2 = {1, 5, 7, 9, 3}
set6.update(set2)
print(set6)
# The object in the update() method does not have to be a set,
# it can be any iterable object (tuples, lists, dictionaries etc.).

mylist = ["kiwi", 4, 7, "coffee"]
set2.update(mylist)
print(set2)
set2.remove(5)
print(set2)

set6.discard("apple")
print(set6)

# Remove the last item by using the pop() method:
set6 = {"apple", "banana", "cherry"}
x = set6.pop()
print(x)
print(set6)

thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

# The union() method returns a new set with all items from
# both sets:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

# The update() method inserts the items in set2 into set1:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

# Both union() and update() will exclude any duplicate items.

