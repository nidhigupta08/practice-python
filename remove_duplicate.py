def remove_duplicates(input_list):
    # Create an empty list to store unique values
    unique_list = []

    # Iterate through the input list
    for item in input_list:
        # If the item is not in the unique list, add it
        if item not in unique_list:
            unique_list.append(item)

    return unique_list


if __name__ == "__main__":
    # Example input list with duplicates
    input_list = [1, 2, 2, 3, 4, 4, 5]

    # Call the remove_duplicates function
    unique_list = remove_duplicates(input_list)

    # Print the unique list
    print("Original list:", input_list)
    print("List with duplicates removed:", unique_list)
