# # Python program to accept n numbers in list and remove duplicates from a list.
# n=int(input("Enter length of list:- "))
# list1=[]
# for i in range(0,n):
#     x=int(input("Enter element at index {}: ".format(i)))
#     list1.append(x)
# print("The original list is:- ",list1)
# list2 = list(set(list1))
# print("The list after removing duplicates:- ",list2)


# #Python program to check if a given key already exists in a dictionary. If key exists relace with anoher key/value pair.
# dict1 = {"OOSE":101,"CPP":201,"JAVA":301,"Python":401}
# key = input("Enter the key value: ")
# if key in dict1.keys():
#     k = input("Enter a new key value: ")
#     v = int(input("Enter a new pair value: "))
#     del dict1[key]
#     dict1.update({k:v})
#     print(dict1)
# else:
#     print("Key is not present in dictionary!")

# # Python program  to accept string and remove the characters which have odd index values of given string using user defined function.
# def odd(str):
#     print("String after removing  characters at odd index value:- ",end=' ')
#     for i in range(len(str)):
#         if(i%2 == 0):
#             print(str[i],end='')
# str = input("Enter a string:- ")
# odd(str)

#Create a list a={1,1,2,3,5,8,13,21,34,55,89} and write a python program that prints out all the elements of the list that are less than 5
a={1,1,2,3,5,8,13,21,34,55,89}
print("List elements that are less than 5: ",end='')
for i in a:
    if i<5:
        print(i,end=' ')
