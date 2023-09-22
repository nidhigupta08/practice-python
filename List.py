#LIST -it can take any data type .15
grocery = ["rice", "Vim bar", "Deo", "pulses", 8]
#print (grocery)
num = [20, 44, 1, 99, 2, 4, 6, 8, 10]
print(num[3])
num.sort()
print(num)
num.reverse()
print(num)
print(min(num))
print(max(num))
num.append(5)
print(num)
num.insert(2, 24)  # 2 means index and 20 will get change to 24
print(num)
num.remove(24)    # remove 24 value from the list.
num.pop()   # it will pop the last element.

names=['John', 'bob', 'mosh', 'Sarah']
print(names)
print(names[-1])  #Sarah
print(names[2:])  #['mosh', 'Sarah']
print(names[1:3])  #['bob', 'mosh']
print(names[: :]) #print all
names[0]='jon'
print(names)

#Write a programs to find the largest number in a list

numbers=[3,6,1,2,8,1,9,6,3,5,12]
max=numbers[0]
for num in numbers:
    if num>max:
        max=num
print(max)
