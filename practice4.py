# Python program  to accept string and remove the characters which have odd index values of given string using user defined function.
def odd(str):
    print("String after removing  characters at odd index value:- ",end=' ')
    for i in range(len(str)):
        if(i%2 == 0):
            print(str[i],end='')
str = input("Enter a string:- ")
odd(str)