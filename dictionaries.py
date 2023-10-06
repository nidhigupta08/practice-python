# Dictionaries
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
prices = {'apple': 0.40, 'banana': 0.50}
my_purchase = {'apple': 1, 'banana': 6}
grocery_bill = sum(prices[fruit] * my_purchase[fruit]
                   for fruit in my_purchase)
print('i owe the grocery $%.2f' %grocery_bill)
# ACCESSING ITEMS
# You can access the items of a dictionary by referring to its key name,
# inside square brackets:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
# There is also a method called get() that will give you the same result:
x = thisdict.get("model")
print(x)
x1 = thisdict.keys()
print(x1)
x2 = thisdict.values()
print(x2)

# The items() method will return each item in a dictionary, as tuples in a list.
x3 = thisdict.items()
print(x3)











