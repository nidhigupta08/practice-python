def find_duplicates(input_list):
    # Create a list to store duplicate values
    duplicates = []

    # Create a set to keep track of unique values
    unique_values = set()

    for item in input_list:
        if item in unique_values:
            # If the item is already in the set, it's a duplicate
            duplicates.append(item)
        else:
            unique_values.add(item)

    return duplicates


if __name__ == "__main__":
    # Example input list with duplicates
    input_list = [1, 2, 2, 3, 4, 4, 5]

    # Call the find_duplicates function
    duplicate_values = find_duplicates(input_list)

    # Print the duplicate values
    print("Original list:", input_list)
    print("Duplicate values:", duplicate_values)
