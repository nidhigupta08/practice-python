# String
course="I m anil's sister." #  'I m anil's sister.' it will give error
course1='I m "anil" sister.' # "I m "anil" sister." it will give error
print(course)
print(course1)

multiple_line='''
Hi Ma'am,
My name is Nidhi gupta and i m looking for a job as a Python developer.

Thank You,
Nidhi Gupta

# '''
print(multiple_line)

# STRING SLICING

# we will use [] to get character at given index.
mystr="nidhi is a good girl"
print(mystr[0:2])
print(mystr[2])
print(mystr[0:5])
print(len(mystr))
# print(mystr[25]) # string index out of range
# print(mystr[0:25])  # it will not give the error  all the string will be printed
print(mystr[0::2])
print(mystr[::])
print(mystr[::3]) # it will print 1st no but it will skip 2 char
print(mystr[::6]) # it will print 1st n   and thn it will skip 5 character n so on .

