# Define a class to represent a to-do list item
class ToDoItem:
  def __init__(self, description, is_completed=False):
    self.description = description
    self.is_completed = is_completed

  def mark_completed(self):
    self.is_completed = True

  def __str__(self):
    status = "Completed" if self.is_completed else "Pending"
    return f"- {self.description} ({status})"

# Define the main to-do list manager function
def manage_todo_list():
  # Initialize an empty list to store to-do items
  todo_list = []

  while True:
    print("\nTo-Do List Manager")
    print("1. Add a new item")
    print("2. View all items")
    print("3. Mark an item as completed")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
      # Add a new item
      description = input("Enter the description of the new item: ")
      new_item = ToDoItem(description)
      todo_list.append(new_item)
      print("Item added successfully!")

    elif choice == "2":
      # View all items
      if not todo_list:
        print("There are no items in your list.")
      else:
        print("\nYour To-Do List:")
        for item in todo_list:
          print(item)

    elif choice == "3":
      # Mark an item as completed
      if not todo_list:
        print("There are no items in your list.")
      else:
        print("\nYour To-Do List:")
        for i, item in enumerate(todo_list):
          print(f"{i+1}. {item}")
        choice = input("Enter the number of the item to mark as completed (or 0 to cancel): ")
        try:
          index = int(choice) - 1
          if 0 <= index < len(todo_list):
            todo_list[index].mark_completed()
            print("Item marked as completed successfully!")
          else:
            print("Invalid item number.")
        except ValueError:
          print("Invalid input. Please enter a number.")

    elif choice == "4":
      # Exit the program
      print("Exiting To-Do List Manager.")
      break

    else:
      print("Invalid choice. Please enter a number between 1 and 4.")

# Start the to-do list manager
manage_todo_list()
