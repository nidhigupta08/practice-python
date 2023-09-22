 #Arithmetic operators
x = 15
y= 4
print('x+y=', x+y)
print('x-y=', x-y)
print('x*y=', x*y)
print('x/y=', x/y)
print('x%y=', x%y)
print('x**y=', x**y)
print('x//y=', x//y)

#ASSIGNMENT OPERATOR is used to assign value to a variables.
x=4
x*=2
print(x)

x=4
x-=2
print(x)

x=4
x+=2
print(x)
x=4
x/=2
print(x)
x=4
x**=2
print(x)
x=4
x//=2
print(x)

# precedence
# parenthesis (), exponentiation 2**3,  multiplication OR division ,  addition OR subtraction
x=10+3*2
print(x)
x=10+3*2**3
print(x)
x=(10+3)*2**2
print(x)

x=(2+3) *10-3   #5*10=5
print(x)

#Logical operator
#AND OR NOT
z=5
print(z>2 and z<10) # both the condition should be true
print(z>2 or z<10)
print(not(z>10))
# Relational
#Bitwise
# Membership operator
# Identity operator.