def add_items_to_list(items):
    """
    Prompts the user for items and adds them to a list using append.
    """
    shopping_list = []
    while True:
        item = input("Enter an item to add to the shopping list (or 'q' to quit): ")
        if item.lower() == 'q':
            break
        else:
            shopping_list.append(item)

    print("\nYour shopping list:")
    for item in shopping_list:
        print(f"- {item}")


# Run the program
add_items_to_list([])  # Create an empty list initially