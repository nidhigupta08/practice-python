def combine_lists(list1, list2):
  """
  Combines two lists using extend to create a new list.
  """
  combined_list = list1.copy()  # Create a copy to avoid modifying the original list1
  combined_list.extend(list2)
  return combined_list

# Example usage
fruits = ["apple", "banana", "orange"]
vegetables = ["carrot", "potato", "broccoli"]

combined_list = combine_lists(fruits, vegetables)

print("Original fruits list:", fruits)
print("Original vegetables list:", vegetables)
print("Combined list using extend:", combined_list)