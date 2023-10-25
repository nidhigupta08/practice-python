# Python program to check if a given key already exists in a dictionary. If key exists relace with anoher key/value pair.
dict1 = {"OOSE":101,"CPP":201,"JAVA":301,"Python":401}
key = input("Enter the key value: ")
if key in dict1.keys():
    k = input("Enter a new key value: ")
    v = int(input("Enter a new pair value: "))
    del dict1[key]
    dict1.update({k:v})
    print(dict1)
else:
    print("Key is not present in dictionary!")

    # OUTPUT
# Enter the key value: CPP
# Enter a new key value: CORE JAVA
# Enter a new pair value: 404
# {'OOSE': 101, 'JAVA': 301, 'Python': 401, 'CORE JAVA': 404}
