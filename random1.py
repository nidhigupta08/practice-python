# The randrange() Function

# The random.randrange() function selects an item randomly from the given range defined by the start,
# the stop, and the step parameters.
# To generate value between a specific range
import random
num = random.randrange(1, 10)
print( num )
num = random.randrange(1, 10, 2)
print( num )

# The choice() Function
# The random.choice() function selects an item from a non-empty series at random.
# To select a random element
import random
random_s = random.choice('Random Module') #a string
print( random_s )
random_l = random.choice([23, 54, 765, 23, 45, 45]) #a list
print( random_l )
random_s = random.choice((12, 64, 23, 54, 34)) #a set
print( random_s )
