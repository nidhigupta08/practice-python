first="aunt"
last="Jennifer"

first_last=first + '[' + last + '] is a coder.'

#formatted string: prefix our string with an 'f' then use curly braces to dynamically insert values into our string.

print(f'{first} [{last}]  is a coder')
print(first_last)
print(last[1:-1])  # print ennife

#String methods

course='python for Beginners'
print(len(course))
print(course.upper())
print(course.lower())
print(course.find('r')) # find() method to find the index of any char
print(course.find('for'))
print(course.replace('beginners', 'absolute beginners'))
print(course.replace('P', 'C'))

#any letter or word is there in the given sentence or not.
print('for'in course)
print(course.title())

print(course.isalnum()) # return false bcz space is there in string"mystr1"
print(course.isalnum()) # return true bcz there is no space

print(course.endswith("ners"))  # True
print(course.endswith("boy"))  # False
print(course.count("o"))        # 3 times "o"
print(course.capitalize())

course1='abcd'
print(course1.isalpha())

course2='avfs'
print(course.isalpha())