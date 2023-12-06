my_list = [1, 2, 2, 3, 4, 4, 5, 5]

unique_elements_dict = {}
for element in my_list:
    unique_elements_dict[element] = True

unique_elements = list(unique_elements_dict.keys())

print(unique_elements)
