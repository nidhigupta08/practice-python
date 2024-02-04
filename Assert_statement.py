# Python provide the assert staement to check if a given logical expression is true or false.Program execution proceeds only
# if the expression is true and raised the AssertionError when it is false.The following code shows the usage of assert not statemet
# num = 10
# assert num>=10   # expression is true so it is executed
# # it got executed successfully
"""
# for even number
try:
    num = int(input("Enter a even number:"))
    assert num %2 ==0   # condition or boolean expression, which gives only true .
    print("the entered number is even")
except AssertionError:  #if i want to handle the assertion error n we caught .  exception raised if num is entered any odd value
    print("Please enter even number")
"""
"""   ASSERT WITHOUT ERROR MESSAGE
def avg(marks):
    assert len(marks)!=0
    return sum(marks)/len(marks)
marks1=[]  #empty list
print("Average of marsk1:", avg(marks1))
"""
"""  ERROR WITH MESSAGE
def avg(marks):
    assert len(marks)!=0, "list is empty"      # message
    return sum(marks)/len(marks)
marks2= [55,88,23,54,12]
print("Average of marks 2 :", avg(marks2))
marks1=[]  #empty list
print("Average of marsk1:", avg(marks1))
"""
"""
# DEGREES  KELVIN  TO FAHRENHEIT
def kelvinToFahrenheit(temp):
    assert temp>=0, "colder than absolute zero"
    return ((temp-273)*1.8)+32
print(kelvinToFahrenheit(273))   # return 32.0
print(int(kelvinToFahrenheit(505.78)))  # return 451
print(kelvinToFahrenheit(-5))  #return assertionError:colder than absolute zero
"""
"""
#calculate avg of list elemnts , not be null, if null raise error.
def listing(l):
    a = len(l)
    assert(a!=0), "list is empty"
    print("Average of lst elements =", sum(l)/a)
l=[]
n=int(input("enter how many elemnts you wnt:"))
for i in range(n):
    num=int(input("Enter elemts in list"))
    assert(num!=0), "element should not be zero"
    l.append(num)
print("enter list is = ",l)
listing(l)

# RESULT
enter how many elemnts you wnt:3
Enter elemts in list23
Enter elemts in list56
Enter elemts in list12
enter list is =  [23, 56, 12]
Average of lst elements = 30.333333333333332
"""
"""
def temptokf(temp):
    ans=temp*9/5+32
    print(ans,"F")
    ans1=temp *9/5-32
    print(ans1,"K")
temp= int(input("Enter temperature: "))
assert(temp>0), "temperature should not be negative value or zero"
temptokf(temp)
"""
fname=input("enter file name tht you wnt to open:=")
assert(fname!=""), "file name should not be null"
with open(fname,"r") as f:
    for line in f.readlines():
        words=line.split()
    for letters in words:
        if(letters.isdigit()):
            print("digit found")
        else:
            print("character found")
