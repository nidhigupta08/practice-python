# WHILE LOOP

i = 0
while(i<45):
    print(i)
    i = i+1


i = 0
while(i<45):
    print(i+1, end=", ")  #it will start printing with 1 to 44 and in a single line (end=" ")
    i = i+1


# BREAK AND CONTINUE
i = 0
while(1):   # if i write 1 or true then it will keep on printing the value
    print(i)
    i = i+1

i = 0
while(True):
    print(i+1, end=" ")
    if(i == 44):
        break
    i = i+1

i = 0         # it start with 5-44
while(True):
    if i < 5:
        i = i+1
        continue

    print(i, end=" ")
    if(i == 44):
        break
    i = i + 1

i = 0   # it prints 5-45
while(True):
    if i+1 < 5:
        i = i+1
        continue

    print(i+1, end=" ")
    if(i == 44):
        break
    i = i + 1

# take input from user until it takes greater then 100 if 100 then print congratulation you have typed greater then 100


while(True):
    num = int(input("Enter a number: "))
    if num > 100:
        print("congratulation you have entered greater then 100. ")
        break
    elif num == 100:
        print("The number is equal to 100")
    else:
        print("Try again")
        continue








