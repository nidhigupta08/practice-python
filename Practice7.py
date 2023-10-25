# Python program to accept n numbers in list and remove duplicates from a list.
n=int(input("Enter length of list:- "))
list1=[]
for i in range(0,n):
    x=int(input("Enter element at index {}: ".format(i)))
    list1.append(x)
print("The original list is:- ",list1)
list2 = list(set(list1))
print("The list after removing duplicates:- ",list2)