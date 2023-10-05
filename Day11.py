import module
from module import kg_to_lbs
from module import find_max
print(kg_to_lbs(70))
print(module.lbs_to_kg(70))

num_max=[3,5,12,45]
print(find_max(num_max))

# find the maximun number
num =[10,3,6,12]
print(max(num))

# OOOOOOOOOOOOOORRRRRRRRRRRRRRR
max= num[0]
for number in num:
    if number>max:
        max=number
print(max)

