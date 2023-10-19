# Code to demonstrate how we can use a lambda function for adding 4 numbers  
add = lambda num: num + 4    
print( add(6) )

# an example of a lambda function that adds 4 to the input number using the add function.
def add( num ):
   return num + 4
print( add(6) )


# an example of a lambda function that multiply 2 numbers and return one result.
a = lambda x, y : (x * y)
print(a(4, 5))

# example of a lambda function that adds 2 numbers and return one result.
a = lambda x, y, z : (x + y + z)
print(a(4, 5, 5))

#Code to calculate the square of each number of a list using the map() function
numbers_list = [2, 4, 5, 1, 3, 7, 8, 9, 10]
squared_list = list(map( lambda num: num ** 2 , numbers_list ))
print( 'Square of each number in the given list:' ,squared_list )