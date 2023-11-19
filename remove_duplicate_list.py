def remove_duplicates(lst):
    return list(set(lst))

original_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = remove_duplicates(original_list)
print("List with duplicates removed:", unique_list)
