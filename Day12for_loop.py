# List using for loop

# list1 = ["Harry", "Nidhi", "Nimi", "Deeps", "Suman"]
list1 = [["Harry", 1], ["Nidhi", 2], ["Nimi", 3], ["Deeps", 4], ["Suman", 5]]   # list of list
for item in list1:
    print(item)  # it will   ['Harry', 1]

for item, quantity in list1:
    print(item, quantity)  # it will print    Harry 1


# Dictionaries using for loop
dict1 = dict(list1)
print(dict1)   # {'Harry': 1, 'Nidhi': 2, 'Nimi': 3, 'Deeps': 4, 'Suman': 5}

for item, quantity in list1:
     print(item, "and lolly is", quantity)
#  OUTPUT
# Harry and lolly is 1
# Nidhi and lolly is 2
# Nimi and lolly is 3
# Deeps and lolly is 4
# Suman and lolly is 5


dict1 = dict(list1)
for item, quantity in dict1.items():
    print(item, "and lolly is ", quantity)
#    items() fun and here we have print the value with the help of dict not list
# Harry and lolly is  1
# Nidhi and lolly is  2
# Nimi and lolly is  3
# Deeps and lolly is  4
# Suman and lolly is  5

dict1 = dict(list1)   # it only prints the key(harry nidhi nimi....)
for item in dict1:
    print(item)


# Quiz
list2 = ["NIDHI", 3, 9, "Kirti", 12, 99, 34, 1, "Nimi", int, float]
for item in list2:
    if str(item).isnumeric() and item > 6:   # int,float is not a string so isnumeric will not read.I typecast item into string.
        print(item)