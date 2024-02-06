# import my_module
#
# print("addition",my_module.add(3,6))
# print("multiplication ", my_module.mult(3,2))
#

# ELSE ONE MORE WAY:
# from my_module import mult
# print("multiplication ",mult(3,2))

# ELSE 2nd  WAY:
# from my_module import mult, add
# print("multiplication ",mult(3,2))
# print("addition",add(3,6))

# other way is doing in interactive interpreter :
# import my_module
# my_module.add(10,20)
# my_module.mult(12,2)

# 3rd way:
from my_module import *
print("multiplication ",mult(3,2))
print("addition",add(3,6))